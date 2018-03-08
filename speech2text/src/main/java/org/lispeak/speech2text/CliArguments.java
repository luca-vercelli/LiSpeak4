package org.lispeak.speech2text;

import com.sampullara.cli.Argument;

public class CliArguments {

	@Argument(description = "Verbose output (to System err)")
	public boolean verbose;

	@Argument(alias = "v", description = "Print version and exit")
	public boolean version;

	@Argument(alias = "h", description = "Print help and exit")
	public boolean help;
}