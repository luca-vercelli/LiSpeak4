package org.lispeak.speech2text;

import java.io.IOException;
import java.io.PrintStream;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;

/**
 * @see https://cmusphinx.github.io/wiki/tutorialsphinx4/#using-sphinx4-in-your-projects
 *
 */
public class AppCli extends LiveSpeechRecognizer {

	public final static String LANG_DEFAULT = "it-IT";

	public static void main(String[] args) throws Exception {

		// TODO some kind of notification to user???
		// TODO how to handle languages?
		// TODO how to trap signals?
		AppCli app = new AppCli();
		app.mainLoop(System.out);
	}

	public AppCli() throws IOException {
		super(getConfiguration(LANG_DEFAULT));
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

}
