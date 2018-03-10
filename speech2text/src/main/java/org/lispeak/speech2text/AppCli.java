package org.lispeak.speech2text;

import java.io.File;
import java.io.IOException;
import java.io.PrintStream;
import java.util.List;
import java.util.prefs.Preferences;

import org.ini4j.Ini;
import org.ini4j.IniPreferences;
import org.ini4j.InvalidFileFormatException;

import com.sampullara.cli.Args;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;

/**
 * @see https://cmusphinx.github.io/wiki/tutorialsphinx4/#using-sphinx4-in-your-projects
 *
 */
public class AppCli {

	public final static String CONFIG_FILE = System.getProperty("user.home") + File.separator + ".lispeak4"; // This works in Windows, too
	public final static String CONFIG_SECTION1 = "General";
	public final static String LANG_DEFAULT = Locale.getDefault().getLanguage();
	public final static String VERSION = "0.1";

	CliArguments options;
	LiveSpeechRecognizer recognizer;
	String lang;

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

		AppCli app = new AppCli();
		app.options = options;

		// TODO some kind of notification to user???
		// TODO how to trap signals?

		app.mainLoop(System.out);
	}

	public AppCli() throws IOException {
		this.lang = getLanguage();
		Configuration configuration = getConfiguration(lang);
		this.recognizer = new LiveSpeechRecognizer(configuration);
	}

	/**
	 * Create a configuration object, assuming all models are under
	 * /speech_recognition/data/&lt;lang&gt;
	 * 
	 * @param lang
	 *            e.g. it-IT
	 * @return
	 */
	public Configuration getConfiguration(String lang) {
		Configuration configuration = new Configuration();

		// configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
		// configuration.setDictionaryPath("resource:/edu/cmu/sphinx/models/en-us/cmudict-en-us.dict");
		// configuration.setLanguageModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us.lm.bin");
		configuration.setAcousticModelPath("resource:/speech_recognition/data/" + lang + "/acoustic-model");
		configuration
				.setDictionaryPath("resource:/speech_recognition/data/" + lang + "/pronounciation-dictionary.dict");
		configuration.setLanguageModelPath("resource:/speech_recognition/data/" + lang + "/language-model.lm");
		// .lm.bin for binay

		return configuration;
	}

	/**
	 * Read data from microphone, print text to output stream
	 * 
	 * @param configuration
	 * @param os
	 * @throws IOException
	 */
	public void mainLoop(PrintStream os) throws IOException {

		// Start recognition process pruning previously cached data.
		recognizer.startRecognition(true);
		SpeechResult result;
		System.err.println("Ready.");
		while ((result = recognizer.getResult()) != null) {
			System.out.format("Hypothesis: %s\n", result.getHypothesis());
			System.err.format("Nbest: %s\n", result.getNbest(6));
			// os.format("Words: %s\n", result.getWords());
			// os.format("Lattica: %s\n", result.getLattice().getNodes());
		}
		// Pause recognition process. It can be resumed then with
		// startRecognition(false).
		recognizer.stopRecognition();
	}

	/**
	 * Temporarily stop recognition.
	 */
	public void stopRecognition() {
		recognizer.stopRecognition();
	}

	/**
	 * Resume recognition, after stopped.
	 */
	public void startRecognition() {
		recognizer.startRecognition(false);
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
