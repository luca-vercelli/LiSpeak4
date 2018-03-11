package org.lispeak.speech2text;

import java.util.Locale;

import com.sampullara.cli.Argument;

public class CliArguments {

	@Argument(description = "Read input from stdin instead of microphone")
	public boolean stdin;

	// FIXME is this useful?
	@Argument(description = "2-letter language. Default is Locale.getDefault().getLanguage()")
	public String lang = Locale.getDefault().getLanguage();

	@Argument(alias = "am", description = "Acoustic model folder")
	public String acousticmodel;

	@Argument(alias = "lm", description = "Language model file (.lm or .lm.bin)")
	public String languagemodel;

	@Argument(alias = "d", description = "Dictionary file (.dict)")
	public String dictionary;

	// FIXME is this useful?
	@Argument(description = "Verbose output (to System err)")
	public boolean verbose;

	@Argument(alias = "v", description = "Print version and exit")
	public boolean version;

	@Argument(alias = "h", description = "Print help and exit")
	public boolean help;
}