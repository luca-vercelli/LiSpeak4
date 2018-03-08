package org.lispeak.speech2text;

import java.io.File;
import java.io.IOException;
import java.io.PrintStream;
import java.util.prefs.Preferences;

import org.ini4j.Ini;
import org.ini4j.IniPreferences;
import org.ini4j.InvalidFileFormatException;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;

/**
 * @see https://cmusphinx.github.io/wiki/tutorialsphinx4/#using-sphinx4-in-your-projects
 *
 */
public class AppCli extends LiveSpeechRecognizer {

	public final static String CONFIG_FILE = System.getProperty("user.home") + File.separator + ".lispeak";
	public final static String CONFIG_SECTION1 = "General";
	public final static String LANG_DEFAULT = "it-IT"; // should be en-EN...

	public static void main(String[] args) throws Exception {

		// TODO some kind of notification to user???
		// TODO how to handle languages?
		// TODO how to trap signals?
		AppCli app = new AppCli();
		app.mainLoop(System.out);
	}

	public AppCli() throws IOException {
		super(getConfiguration(getLanguage()));
	}

	/**
	 * Create a configuration object, assuming all models are under
	 * /speech_recognition/data/&lt;lang&gt;
	 * 
	 * @param lang
	 *            e.g. it-IT
	 * @return
	 */
	public static Configuration getConfiguration(String lang) {
		Configuration configuration = new Configuration();

		// configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
		// configuration.setDictionaryPath("resource:/edu/cmu/sphinx/models/en-us/cmudict-en-us.dict");
		// configuration.setLanguageModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us.lm.bin");
		configuration.setAcousticModelPath("resource:/speech_recognition/data/" + lang + "/acoustic-model");
		configuration
				.setDictionaryPath("resource:/speech_recognition/data/" + lang + "/pronounciation-dictionary.dict");
		configuration.setLanguageModelPath("resource:/speech_recognition/data/" + lang + "/language-model.lm"); // .lm.bin
																												// for
																												// binay

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
		startRecognition(true);
		SpeechResult result;
		System.err.println("Ready.");
		while ((result = getResult()) != null) {
			os.format("Hypothesis: %s\n", result.getHypothesis());
			os.format("Nbest: %s\n", result.getNbest(6));
			// os.format("Words: %s\n", result.getWords());
			// os.format("Lattica: %s\n", result.getLattice().getNodes());
		}
		// Pause recognition process. It can be resumed then with
		// startRecognition(false).
		stopRecognition();
	}

	/**
	 * Read language from configuration file
	 * @return
	 */
	public static String getLanguage() {
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
