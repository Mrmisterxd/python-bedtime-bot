<div align="center">
<h1> <a href="https://github.com/Mrmisterxd/python-bedtime-bot">Bed Time Bot</a> </h1> 

<p>This is a simple Telegram bot code that will help you turn off your computer without getting out of bed or set a shutdown timer.</p>

</div>

## ℹ️ How to use the bot?
- You need to create your own bot in @BotFather
- Download all the necessary libraries (there's only **one**, `pyTelegramBotAPI`)
- After that, you take the token that the bot gave you and paste it into my code (at the beginning, the inscription here_you_token will be visible)
- After that, you run my Python script by double-clicking (duh!) and everything works.

## ℹ️ Description of choosing:
### `1. Set bedtime in seconds` 
- Sets a sleep timer for Windows in seconds. 
*It executes the command in Win+R; your value = `"shutdown -s -t <your value>"` entered in Win+R is in seconds.*

### `2. Turn off bedtime` 
- Turns off the sleep timer. 
*The meaning of this command in Win+R is `"shutdown -a"`*

### `3. Set bedtime in hours` 
- Sets a sleep timer for Windows in hours.
*It executes the command in Win+R; your value in `"shutdown -s -t <your value>"` will be seconds multiply 3600.*

### `4. Set bedtime in minutes` 
- Sets a sleep timer for Windows in minutes.
*It executes the command in Win+R; your value in `"shutdown -s -t <your value>"` will be seconds multiply 60.*

### `5. Off pc` 
- Immediately shuts down your PC. 
- **Confirmation required**: The bot will ask "Are you sure?" to prevent accidental shutdowns.
>[!WARNING]
>### This command uses the `-f` (force) flag. 
>Windows will **forcefully close** all running applications without saving. Unsaved work in Word, Excel, or your browser will be **LOST**.
>[!NOTE]
>### Important System Rule:
>- **Conflict of commands**: Windows does not allow setting a new timer if one is already running. If you want to change the time (e.g., from 60 to 30 minutes), you **must** click `Turn off bedtime` first to reset the system queue. 
>- **Admin Rights**: Depending on your system settings, you might need to run the Python script as an **Administrator** for the `shutdown` commands to work properly.

### `6. Check bedtime` 
>[!IMPORTANT]
> ### Displays the timer set during the current session. It cannot detect timers set via Win+R or previous script runs or another script/programm.
-  This item is <ins>***ONLY***</ins> needed to calm your mind after you set the sleep time or disable it (<ins>***During the first program launch, only after selecting any of the preceding options❗***</ins>).
-  *If* you set the sleep time during a different previous launch of this program this information is also *incorrect*.
-  As I said, the information is ***only*** valid during a single program launch. *If* you set the sleep time using Win+R, this is ***also***  *incorrect*.
>[!NOTE]
>### All correct information is:
> - 1 - only after selecting any of the options
> - 2 - only during a single program launch.

## ℹ️ Compatibility with operating systems:
- This program is only compatible with Windows
> Windows XP, Vista, 7, 8, 8.1, 10, 11

## ⚖️ Licensing

The project is distributed under the [MIT License](https://github.com/Mrmisterxd/bed-time/blob/main/LICENSE)
