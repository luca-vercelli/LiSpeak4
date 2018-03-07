package org.lispeak.speech2text;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.LiveSpeechRecognizer;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;

/**
 * @see https://cmusphinx.github.io/wiki/tutorialsphinx4/#using-sphinx4-in-your-projects
 *
 */
public class AppCli {

	public final static String LANG_DEFAULT = "it-IT";
	
	public static void main(String[] args) throws Exception {

		// TODO some kind of notification to user???
		// TODO how to handle languages?
		// TODO how to trap signals?
		
		new AppCli();
		
	}

	public AppCli() throws IOException {
		Configuration configuration = getConfiguration(LANG_DEFAULT);

		microphoneToStream(configuration, System.out);
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
	public void microphoneToStream(Configuration configuration, PrintStream os) throws IOException {

		LiveSpeechRecognizer recognizer = new LiveSpeechRecognizer(configuration);
		// Start recognition process pruning previously cached data.
		recognizer.startRecognition(true);
		SpeechResult result;
		System.err.println("Ready.");
		while ((result = recognizer.getResult()) != null) {
			os.format("Hypothesis: %s\n", result.getHypothesis());
			os.format("Nbest: %s\n", result.getNbest(6));
			// os.format("Words: %s\n", result.getWords());
			// os.format("Lattica: %s\n", result.getLattice().getNodes());
		}
		// Pause recognition process. It can be resumed then with
		// startRecognition(false).
		recognizer.stopRecognition();
	}

	/**
	 * Read data from audio input stream, print text to output stream
	 * 
	 * @param configuration
	 * @param is
	 * @param os
	 * @throws IOException
	 */
	public void streamToStream(Configuration configuration, InputStream is, PrintStream os) throws IOException {

		StreamSpeechRecognizer recognizer = new StreamSpeechRecognizer(configuration);
		// Start recognition process pruning previously cached data.
		recognizer.startRecognition(is);
		SpeechResult result;
		while ((result = recognizer.getResult()) != null) {
			os.format("Hypothesis: %s\n", result.getHypothesis());
		}
		// Pause recognition process. It can be resumed then with
		// startRecognition(false).
		recognizer.stopRecognition();
	}

}
