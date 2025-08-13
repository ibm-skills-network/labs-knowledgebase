---
sidebar_position: 3
---

import TOCInline from '@theme/TOCInline';

# Troubleshooting

:::warning
<h2> Issues with copy/paste in labs' Vim editor on Linux/Windows </h2>
<!-- Use HTML heading here so it is not detected (and thus shown redundantly) by the Table of Contents below -->

We are aware of limitations with the copy/paste functionality on Linux and Windows when using the Vim editor
within a lab. \
We request that you manually type for now until these are resolved and the *Press to Type* button works as intended.
Thanks!
:::

<h2>Table of contents</h2>
<!-- Use HTML heading here so it is not detected (and thus shown redundantly) by the Table of Contents below -->
<TOCInline toc={toc} />

## Common issues

### `Cannot connect to Docker daemon` in Cloud IDE

If you are getting an error similar to the following when trying to run `docker version`:

```sh
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

You need to be using **Cloud IDE with Kubernetes** (which will appear in your command prompt as `theiadocker`)
instead of the regular Cloud IDE (which appears in your command prompt as "just" `theia`).

:::tip

A good way to check if you're using the correct version of Cloud IDE is to check your **command prompt**
in the lab's terminal (which you can quickly launch using `CTRL`+`SHIFT`+`` ` `` within the lab):

- If you see `theia@theia-[username]`, you are using the "regular" Cloud IDE ❌
- If you see `theiadocker@theia-[username]`, you are using Cloud IDE wth Kubernetes ✅

:::

### I can't open my application in the browser in Cloud IDE

1. Look for the **Skills Network Toolbox** icon at the bottom of the menu bar located on the left side of the IDE.

2. Then click on **"Launch Your Application"**.

3. In the "Application Port" field, enter the port number your application is running from the given instruction.

4. Click the **"Your Application"** button to open your application in the browser.

### `Port already in use` error when restarting server

1. Kill the process occupying the port your server is trying to use using the following command:

    ```sh
    kill -9 $(lsof -t -i :[YOUR SERVER'S PORT NUMBER])
    ```

    :::note
    For example, to kill the process using port 3000, you should run `kill -9 $(lsof -t -i :3000)`
    :::

1. Restart your server.

### I did not receive a grade or see completion marked for a lab I finished

Please note that **practice labs are ungraded** and are hence not marked as completed.
If you're sure the lab was *not* for practice, then please submit a support ticket using Tai.

### I don't know how to mark my lab as complete

:::info Important
**Lab completion must be registered from your original Learning Management System (LMS), not from within the lab environment.**

When you finish a lab:
- **Do NOT** look for a completion button inside the lab
- **Return to your original course platform** (the LMS you came from) to mark the lab as complete
:::

### `Error occurred while trying to proxy` when accessing application

If you encounter an error message like the following:

- `Error occurred while trying to proxy: [IP address]:[port]/` 
- for example, `Error occurred while trying to proxy: 172.17.52.96:8888/`

this error message indicates that the application you're trying to access is not running or is otherwise not accepting traffic. If the lab instructions instructed you to run a command to start your application, please confirm you've run the command and it was successful before trying to access your application.

### I can't change the model used in my chat in AI Classroom

- Please note that in AI Classroom, you can't change the model used for a chat after you send your first message.
- To use a different model, you'll need to create a new chat.

### I can't download .ipynb in JupyterLite

1. **Right-click**  (or option-click on mac) the notebook file in the file browser.
2. Select **"Download"** from the context menu.

![Download notebook option](/img/download(ipynb).png)

### Lab not loading (loading sign is stagnant)

If your lab appears to be stuck on a loading screen or the loading indicator (like the skills network tree) remains stagnant, try the following troubleshooting steps in order:

1. **Refresh the page**
   - Press `F5` or `Ctrl+R` (Windows/Linux) / `Cmd+R` (Mac) to refresh the browser page

2. **Clear browser cache and cookies**
   - Open your browser's developer tools (`F12` or `Ctrl+Shift+I`)
   - Right-click the refresh button and select "Empty Cache and Hard Reload"
   - Or manually clear cookies and cache from your browser settings

3. **Try a different browser**
   - Switch to a different browser (Chrome, Firefox, Safari, Edge)
   - Ensure you're using the latest version of the browser

4. **Restart the lab**
   - Close the lab tab completely
   - Return to your course platform
   - Re-launch the lab from the original link

5. **Check your internet connection**
   - Ensure you have a stable internet connection
   - Try disabling VPN if you're using one
   - Test your connection speed

7. **Create a support ticket**
   - If none of the above steps work, the issue may be on our end
   - Submit a support ticket with details about your browser, operating system, and the steps you've already tried

### Lab loaded but not working

If your lab has loaded successfully but you're experiencing issues with functionality, tools not working, or unexpected behavior, try the following:

1. **Use the Reset Lab button**
   - Look for the **Reset Lab** button at the bottom left of your screen
   - Click on it to reset your lab environment to a clean state
   - This will clear any corrupted files or configurations that might be causing issues

![Reset Lab button](/img/reset.png)

2. **If the reset doesn't help**
   - Try the troubleshooting steps from the [Lab not loading](#lab-not-loading-loading-sign-is-stagnant) section above
   - Contact support if the issue persists

## General troubleshooting

:::info

Please first attempt to look up your issue in the [Common Issues](#common-issues) section above before
trying the steps below or opening a support ticket.

:::

### General server errors

For other server-related errors:

- Simply refresh the entire page in your browser
- If the problem persists, try restarting your application from the terminal
- Otherwise, ask to open a support ticket

### Application not loading

If your application fails to load or displays errors:

- Verify that you have completed all prerequisite steps in the lab instructions
- Check the terminal for any error messages
- Ensure all required dependencies are installed
- Restart your application and try again
- Otherwise, ask to open a support ticket