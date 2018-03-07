package org.lispeak.speech2text;

import java.awt.AWTException;
import java.awt.CheckboxMenuItem;
import java.awt.Image;
import java.awt.Menu;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.SystemTray;
import java.awt.Toolkit;
import java.awt.TrayIcon;
import java.awt.TrayIcon.MessageType;
import java.io.IOException;
import java.net.URL;

import javax.swing.ImageIcon;

/**
 * @see https://cmusphinx.github.io/wiki/tutorialsphinx4/#using-sphinx4-in-your-projects
 *
 */
public class AppGui extends AppCli {

	public final static String LANG_DEFAULT = "it-IT";

	TrayIcon trayIcon;

	public static void main(String[] args) throws Exception {

		// TODO some kind of notification to user???
		// TODO how to handle languages?
		// TODO how to trap signals?

		AppGui app = new AppGui();
		app.mainLoop(System.out);

	}

	public AppGui() throws IOException {
		// recognition already started here
		showIconInSystemTray();
	}

	public void showIconInSystemTray() {
		if (!SystemTray.isSupported()) {
			System.err.println("SystemTray is not supported");
			return;
		}
		final PopupMenu popup = new PopupMenu();
		Image image = createImage("/listen.png","system tray");
				//Toolkit.getDefaultToolkit().createImage(getClass().getResource("listen.png"));
		trayIcon = new TrayIcon(image);
		final SystemTray tray = SystemTray.getSystemTray();

		// Create a pop-up menu components
		MenuItem aboutItem = new MenuItem("About");
		CheckboxMenuItem cb1 = new CheckboxMenuItem("Set auto size");
		CheckboxMenuItem cb2 = new CheckboxMenuItem("Set tooltip");
		Menu displayMenu = new Menu("Display");
		MenuItem errorItem = new MenuItem("Error");
		MenuItem warningItem = new MenuItem("Warning");
		MenuItem infoItem = new MenuItem("Info");
		MenuItem noneItem = new MenuItem("None");
		MenuItem exitItem = new MenuItem("Exit");

		// Add components to pop-up menu
		popup.add(aboutItem);
		popup.addSeparator();
		popup.add(cb1);
		popup.add(cb2);
		popup.addSeparator();
		popup.add(displayMenu);
		displayMenu.add(errorItem);
		displayMenu.add(warningItem);
		displayMenu.add(infoItem);
		displayMenu.add(noneItem);
		popup.add(exitItem);

		trayIcon.setPopupMenu(popup);

		try {
			tray.add(trayIcon);
		} catch (AWTException e) {
			System.err.println("TrayIcon could not be added.");
		}
	}

	// Obtain the image URL
	// This code from Oracle should be avoided
	protected Image createImage(String path, String description) {
		URL imageURL = this.getClass().getResource(path);

		if (imageURL == null) {
			System.err.println("Resource not found: " + path);
			return null;
		} else {
			return (new ImageIcon(imageURL, description)).getImage();
		}
	}

	public void showNotification(String title, String msg, MessageType type) {
		trayIcon.displayMessage(title, msg, type);
	}

	public void showNotification(String title, String msg) {
		showNotification(title, msg, MessageType.INFO);
	}

	public void showNotification(String title) {
		showNotification(title, "", MessageType.INFO);
	}

}
