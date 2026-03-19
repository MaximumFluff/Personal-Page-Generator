article_name: Tiling window managers part 2: 2 Hyprland 2 Furious: Config drift
date_created: 18/03/2026
date_modified: 19/03/2026

Due to some regressions in COSMIC, I had moved back to KDE for some months, finding myself missing the tiling features but afraid of the potentially daunting task of configuring one. Turns out, getting a functional [Hyprland](https://hypr.land) config wasn't the pain I thought it was.

## The setup
---

Reading documentation is one of the most important skills a developer can have. There is no better test of this than reading the Hyprland wiki when installing. The base package itself does not come with everything one would want and there is a remarkable amount of choice that goes into customizing your Hyprland setup.

Luckily, the wiki is one of the easiest to read I've seen to date and contains good examples of default configurations. Getting a functional setup took significantly less time than anticipated (I set aside an entire Sunday for this task, expecting pain and misery!)

I went with Hyprpanel for my top bar (as it comes pretty full featured out of the box), Hyprpaper for wallpapers, Hyprlock for screen locking, Hypridle for handling automatic suspending, and Walker as the application launcher.

Important to note, make sure you check if any part of the Hyprland ecosystem you choose to install has any sub-dependencies that need installing or configuring.

I recently had created a bootstrap script for Arch Linux, allowing me to install all the packages I desire from a fresh install.
My next step after installation and copying over the default configurations was installing the packages then adding them to my script.

```bash
packages=(
  ...
  hyprland
  hyprpaper
  hyprpicker
  hypridle
  hyprlock
  swww
  xdg-desktop-portal-hyprland
  brightnessctl
  hyprpolkitagent
)

echo "Installing system packages now..."
sudo pacman -Syu
sudo pacman -S "${packages[@]}"

# Some packages are required to be installed from the AUR

yayPackages=(
  ags-hyprpanel-git
  walker
  grimblast
  elephant
  elephant-desktopapplications
  qtct6-kde
)

yay -S "${yayPackages[@]}" 
```

## Configuration and GNU Stow
---

### The config part
---

My current setup is running 95% default configuration options. Every part of Hyprland either comes with a default configuration or the wiki will have one that you can copy and paste. The only significant changes I've made is that I removed window rounding from window borders and added some keybinds I missed from COSMIC:

```bash
# .config/hypr/hyprland.conf
# Move active window left/right/up/down
bind = $mainMod SHIFT, left, movewindow, l
bind = $mainMod SHIFT, right, movewindow, r
bind = $mainMod SHIFT, up, movewindow, u
bind = $mainMod SHIFT, down, movewindow, d
# Open browser
bind = $mainMod, B, exec, $browser
```

### The GNU Stow part
---

GNU Stow is a fancy little program I've been using, that has been described as a "dotfile farm manager"

The short explanation is this: I have all my config files in my home folder called "Dotfiles". Running the command `gnu stow .` in that directory generates symlinks to all those files inside my Home folder. So for example, after running that stow command, inside `/home/alex/.config/hypr/hyprland.conf` there will be a symlink that links to the file inside `/home/alex/Dotfiles/.config/hypr/hyprland.conf`

If you find my explanation lacking, you can [read a better one from the blog of Brandon Invergo](https://brandon.invergo.net/news/2012-05-26-using-gnu-stow-to-manage-your-dotfiles.html)

What this allows for me, is my dotfiles are now managed with Git, along with my install script. As part of the script, my dotfiles are copied over and stowed after package installation. When installing Arch on my laptop, I had my setup ready to go within minutes of the OS install finishing.

### The actual dotfiles
---

You can browse my dotfiles [over here on GitHub](https://github.com/MaximumFluff/dotfiles) to get a better idea of my setup.

## The experience
---

Good lord, and I thought COSMIC was smooth! Hyprland is lightning fast, quite lightweight and customizable to an almost infinite amount! Within an hour of using it I knew it was going to be my daily driver. I can tell why customizing and posting Hyprland configurations to Reddit has become such a popular pasttime.

I'm truly glad I got over my dotfile phobia and dove into it. For any developer and/or fan of keyboard shortcuts, you need to give it a try!
