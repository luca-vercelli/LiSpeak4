package org.lispeak.speech2text;

import static spark.Spark.*;

import spark.Request;

public class AppREST {

	public static void main(String[] args) {
		// port should be declared here, using port(4567)
		get("/startServer", (req, res) -> startServer(req));
		get("/stopServer", (req, res) -> stopServer(req));
		get("/pauseServer", (req, res) -> pauseServer(req));
		get("/changeLanguage", (req, res) -> changeLanguage(req));
	}

	protected static String startServer(Request req) {
		// TODO
		init();
		return "";
	}

	protected static String stopServer(Request req) {
		stop();
		return ""; // WON'T return...
	}

	protected static String pauseServer(Request req) {
		//TODO
		return ""; // WON'T return...
	}

	protected static String changeLanguage(Request req) {
		// TODO
		return "";
	}
}
