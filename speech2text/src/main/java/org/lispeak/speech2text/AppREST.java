package org.lispeak.speech2text;

import static spark.Spark.*;

import java.io.IOException;
import java.util.List;

import com.sampullara.cli.Args;

import spark.Request;

public class AppREST extends AppCli {

	public static void main(String[] args) throws IOException {

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
	}

	protected void startWebServer() {
		// port should be declared here, using port(4567)
		get("/startServer", (req, res) -> startServer(req));
		get("/stopServer", (req, res) -> stopServer(req));
		get("/pauseServer", (req, res) -> pauseServer(req));
		get("/changeLanguage", (req, res) -> changeLanguage(req));
	}

	protected String startServer(Request req) {
		// TODO
		init();
		return "";
	}

	protected String stopServer(Request req) {
		stop();
		return ""; // WON'T return...
	}

	protected String pauseServer(Request req) {
		// TODO
		return ""; // WON'T return...
	}

	protected String changeLanguage(Request req) throws IOException {
		pauseRecognition();

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

		createRecognizer();
		//mainLoop();				//?!?
		return "";
	}
}
