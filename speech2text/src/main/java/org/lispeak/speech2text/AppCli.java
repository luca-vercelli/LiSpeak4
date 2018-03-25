package org.lispeak.speech2text;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Locale;
import java.util.prefs.Preferences;

import org.ini4j.Ini;
import org.ini4j.IniPreferences;
import org.ini4j.InvalidFileFormatException;

import com.sampullara.cli.Args;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;

/**
 * Recognized speech is sent to Standard Output. All other messages to Standard
 * Error.
 * 
 * @see https://cmusphinx.github.io/wiki/tutorialsphinx4/#using-sphinx4-in-your-projects
 *
 */
public class AppCli {

	public final static String CONFIG_FILE = System.getProperty("user.home") + File.separator + ".lispeak4";
	public final static String CONFIG_SECTION1 = "General";
	public final static String LANG_DEFAULT = Locale.getDefault().getLanguage();
	public final static String VERSION = "0.1";

	CliArguments options;
	LiveSpeechRecognizer micRecognizer;
	StreamSpeechRecognizer streamRecognizer;

	public static void main(String[] args) throws Exception {

		CliArguments options = new CliArguments();
		List<String> arguments = Args.parseOrExit(options, args);

		if (options.version) {
			System.err.println("Version " + VERSION);
			return;
		}

		if (options.help) {
			Args.usage(CliArguments.class);
			return;
		}

		if (arguments.size() > 0) {
			System.err.println("Unexpected arguments");
			Args.usage(CliArguments.class);
			System.exit(1);
		}

		AppCli app = new AppCli(options);

		// TODO some kind of notification to user???
		// TODO how to trap signals?

		app.mainLoop();
	}

	public AppCli(CliArguments options) throws IOException {
		this.options = options;
		
		if (this.options.lang == null)
			this.options.lang = getLanguage();
		Configuration configuration = getConfiguration();

		if (this.options.stdin)
			this.streamRecognizer = new StreamSpeechRecognizer(configuration);
		else
			this.micRecognizer = new LiveSpeechRecognizer(configuration);
	}

    private String searchModelsDir(String lang) {
        String[] trials = {
                "~/.local/share/sphinx-lispeak-" + options.lang,
                "/usr/local/share/sphinx-lispeak-" + options.lang,
                "/usr/share/sphinx-lispeak-" + options.lang
                };
        for (String trial: trials)
            if (new File(trial).exists())
                return trial;
        throw new IllegalArgumentException("Folder not found for language: " + lang);
    }

	/**
	 * Create a configuration object from options
	 * 
	 * @return
	 */
	public Configuration getConfiguration() {
		Configuration configuration = new Configuration();
        String dir = searchModelsDir(options.lang);

		if (options.acousticmodel == null)
			options.acousticmodel = dir + "/acoustic-model";
		if (options.dictionary == null)
			options.dictionary = dir + "/pronounciation-dictionary.dict";
		if (options.languagemodel == null)
			options.languagemodel = dir + "/language-model.lm";

		configuration.setAcousticModelPath(options.acousticmodel);
		configuration.setDictionaryPath(options.dictionary);
		configuration.setLanguageModelPath(options.languagemodel);

		return configuration;
	}

	public void mainLoop() throws IOException {

		if (options.stdin)
			mainLoopStream();
		else
			mainLoopMic();
	}

	/**
	 * Read data from microphone, print text to stdout
	 * 
	 * @param configuration
	 * @param os
	 * @throws IOException
	 */
	protected void mainLoopMic() throws IOException {

		// Start recognition process pruning previously cached data.
		micRecognizer.startRecognition(true);
		SpeechResult result;
		System.err.println("Ready.");
		while ((result = micRecognizer.getResult()) != null) {
			System.out.println(result.getHypothesis());
			System.err.format("Nbest: %s\n", result.getNbest(6));
			// os.format("Words: %s\n", result.getWords());
			// os.format("Lattica: %s\n", result.getLattice().getNodes());
		}
		// Pause recognition process. It can be resumed then with
		// startRecognition(false).
		micRecognizer.stopRecognition();
	}

	/**
	 * Read data from stdin, print text to stdout
	 * 
	 * @param configuration
	 * @param os
	 * @throws IOException
	 */
	protected void mainLoopStream() throws IOException {

		streamRecognizer.startRecognition(System.in);
		SpeechResult result;
		System.err.println("Ready.");
		while ((result = streamRecognizer.getResult()) != null) {
			System.out.println(result.getHypothesis());
			System.err.format("Nbest: %s\n", result.getNbest(6));
			// os.format("Words: %s\n", result.getWords());
			// os.format("Lattica: %s\n", result.getLattice().getNodes());
		}
		// Pause recognition process. It can be resumed then with
		// startRecognition(false).
		streamRecognizer.stopRecognition();
	}

	/**
	 * Read language from configuration file
	 * 
	 * @return
	 */
	public String getLanguage() {
		Preferences fileini = null;
		try {
			fileini = getIniFile();
		} catch (InvalidFileFormatException e) {
			System.err.println("Invalid configuration file. It will be ignored.");
		} catch (IOException e) {
			System.err.println("I/O error reading configuration file. It will be ignored.");
		}
		String lang = (fileini != null) ? fileini.node(CONFIG_SECTION1).get("lang", LANG_DEFAULT) : null;
		return lang;
	}

	/**
	 * Read the whole configuration file.
	 * 
	 * @return
	 * @throws InvalidFileFormatException
	 * @throws IOException
	 */
	public static Preferences getIniFile() throws InvalidFileFormatException, IOException {
		File fileini = new File(CONFIG_FILE);
		if (!fileini.exists())
			return null;
		Ini ini = new Ini(fileini);
		return new IniPreferences(ini);
	}
}
