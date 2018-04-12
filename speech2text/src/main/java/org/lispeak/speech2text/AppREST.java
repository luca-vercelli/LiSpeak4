package org.lispeak.speech2text;

import static spark.Spark.get;
import static spark.Spark.stop;

import java.io.IOException;

import spark.Request;

public class AppREST extends AppCli {

	public static void main(String[] args) throws IOException {

		CliArguments options = defaultArgumentsHandling(args);	

		AppREST app = new AppREST(options);

		// TODO some kind of notification to user???
		// TODO how to trap signals?

		app.mainLoop();
	}

	public AppREST(CliArguments options) throws IOException {
		super(options);
	}

	@Override
	public void mainLoop() throws IOException {
		startWebServer();
		super.mainLoop();
		stop();
	}

	protected void startWebServer() {
		// port should be declared here, using port(4567)
		get("/changeLanguage", (req, res) -> changeLanguage(req));
	}

	protected String changeLanguage(Request req) throws IOException {
		requestPauseRecognition();

		String lang = req.attribute("lang");
		String acousticModel = req.attribute("acousticModel");
		String languageModel = req.attribute("languageModel");
		String dictionary = req.attribute("dictionary");

		if (lang != null && !"".equals(lang.trim()))
			options.lang = lang.trim();
		if (acousticModel != null && !"".equals(acousticModel.trim()))
			options.acousticmodel = acousticModel.trim();
		if (languageModel != null && !"".equals(languageModel.trim()))
			options.languagemodel = languageModel.trim();
		if (dictionary != null && !"".equals(dictionary.trim()))
			options.dictionary = dictionary.trim();

		requestResumeRecognition();
		
		return "";
	}
}
