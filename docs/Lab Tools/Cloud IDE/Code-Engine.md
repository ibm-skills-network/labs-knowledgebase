# Code Engine Reference

The **Code Engine** is a plugin for the IBM Cloud that lets you manage **projects**, **applications**, **jobs**, and **functions** in IBM Cloud Code Engine directly from the terminal.

This guide assumes you are working inside the provided cloud IDE environment.  
No login/logout is required — authentication is already handled for you.

## Basic Concepts:

- **Project** – a workspace that groups your apps, jobs, and functions, users should not access this.  
- **Application (App)** – a containerized service that scales automatically based on requests.  
- **Job** – a one-off or recurring workload that runs to completion.  
- **Function** – lightweight serverless functions.

## General CLI Structure

All Code Engine commands use:

```bash
ibmcloud ce <resource> <action> [flags]
```

Examples:

```bash
#Current Project Info
ibmcloud ce project current

#Create Sample Hello World Application
ibmcloud ce application create --name myapp --image icr.io/codeengine/hello

#Create Sample Hello World Application from Source
ibmcloud ce application create --name myapp --build-source https://github.com/IBM/CodeEngine --build-context-dir helloworld --image us.icr.io/${SN_ICR_NAMESPACE}/helloworld --registry-secret icr-secret

#Create Application from Your Image
ibmcloud ce application create --name myapp --image us.icr.io/${SN_ICR_NAMESPACE}/yourimage:tag --registry-secret icr-secret
```

---

### `ibmcloud ce application bind`

  Bind an IBM Cloud service instance to an application.

  **Syntax**

  ```bash
  ibmcloud ce application bind --name APP_NAME (--service-instance SI_NAME |
  --service-instance-id SI_ID) [--no-wait] [--prefix PREFIX] [--quiet] [--role ROLE]
  [--service-credential SERVICE_CREDENTIAL] [--wait] [--wait-timeout WAIT_TIMEOUT]
  ```

  #### Command Options

  **Required Options**

  **`--name, -n`**
  The name of the application to bind. This value is required.

  **Service Instance Options**

  **`--service-instance, --si`**
  The name of an existing IBM Cloud service instance to bind to the application. This value is
   optional.

  **`--service-instance-id, --siid`**
  The GUID of an existing IBM Cloud service instance to bind to the application. This value is
   optional.

  **Service Credential Options**

  **`--service-credential, --sc`**
  The name of an existing service credential to use for this service binding. If you do not
  specify a service instance credential, new credentials are generated during the bind action.
   This value is optional.

  **`--role, -r`**
  The name of a service role for the new service credential that is created for this service
  binding. Valid values include `Reader`, `Writer`, `Manager`, or a service-specific role. The
   option defaults to `Manager` or the first role provided by the service if `Manager` is not
  supported. This option is ignored if `--service-credential` is specified. This value is
  optional.

  **Wait Options**

  **`--wait, -w`**
  Bind the service instance and wait for the service binding to be ready. If you specify the
  `--wait` option, the application bind waits for a maximum time in seconds, as set by the
  `--wait-timeout` option, for the app bind to complete successfully. If the app bind is not
  completed successfully or fails within the specified `--wait-timeout` period, the command
  fails. This value is optional. The default value is `true`.

  **`--no-wait, --nw`**
  Bind the service instance and do not wait for the service binding to be ready. If you
  specify the `--no-wait` option, the service binding creation is started and the command
  exits without waiting for it to complete. Use the `app get` command to check the application
   bind status. This value is optional. The default value is `false`.

  **`--wait-timeout, --wto`**
  The length of time in seconds to wait for the service binding to be ready. This value is
  required if the `--wait` option is specified. This value is ignored if the `--no-wait`
  option is specified. The default value is `300`.

  **Other Options**

  **`--prefix, -p`**
  A prefix for environment variables that are created for this service binding. Must contain
  only uppercase letters, numbers, and underscores (`_`), and cannot start with a number. This
   value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default
   value is `false`.

---

### `ibmcloud ce application create`

  Create an application.

  **Syntax**

```bash
  ibmcloud ce application create --name APP_NAME ((--image IMAGE_REF | (--build-source SOURCE
  [--image IMAGE_REF])) [--argument ARGUMENT] [--build-commit BUILD_COMMIT]
  [--build-context-dir BUILD_CONTEXT_DIR] [--build-dockerfile BUILD_DOCKERFILE]
  [--build-git-repo-secret BUILD_GIT_REPO_SECRET] [--build-size BUILD_SIZE] [--build-strategy
  BUILD_STRATEGY] [--build-timeout BUILD_TIMEOUT] [--cluster-local] [--command COMMAND]
  [--concurrency CONCURRENCY] [--concurrency-target CONCURRENCY_TARGET] [--cpu CPU] [--env
  ENV] [--env-from-configmap ENV_FROM_CONFIGMAP] [--env-from-secret ENV_FROM_SECRET]
  [--ephemeral-storage EPHEMERAL_STORAGE] [--force] [--max-scale MAX_SCALE] [--memory MEMORY]
  [--min-scale MIN_SCALE] [--mount-configmap MOUNT_CONFIGMAP] [--mount-data-store
  MOUNT_DATA_STORE] [--mount-secret MOUNT_SECRET] [--no-cluster-local] [--no-wait] [--output
  OUTPUT] [--port PORT] [--probe-live PROBE_LIVE] [--probe-ready PROBE_READY] [--quiet]
  [--registry-secret REGISTRY_SECRET] [--request-timeout REQUEST_TIMEOUT] [--revision-name
  REVISION_NAME] [--scale-down-delay SCALE_DOWN_DELAY] [--service-account SERVICE_ACCOUNT]
  [--trusted-profiles-enabled] [--user USER] [--visibility VISIBILITY] [--wait]
  [--wait-timeout WAIT_TIMEOUT]
```

  #### Command Options

  **Required Options**

  **`-n, --name`**
  The name of the application. Use a name that is unique within the project.
  - The name must begin with a lowercase letter.
  - The name must end with a lowercase alphanumeric character.
  - The name must be 63 characters or fewer and can contain lowercase letters, numbers, and
  hyphens (`-`).

  This value is required.

  **Image and Build Options**

  **`--image, -i`**
  The name of the image that is used for this application. The format is
  `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are optional. If `REGISTRY`
  is not specified, the default is `docker.io`. If `TAG` is not specified, the default is
  `latest`. The image option is required if the `--build-source` option is not specified. This
   value is optional.

  **`--build-source, --source, --bsrc, --src`**
  The URL of the Git repository or the path to local source that contains your source code;
  for example `https://github.com/IBM/CodeEngine` or `.`. This value is optional.

  **`--build-commit, --commit, --bcm, --cm, --revision`**
  The commit, tag, or branch in the source repository to pull. The build commit option is
  allowed only if the `--build-source` option is set. This value is optional.

  **`--build-context-dir, --context-dir, --bcdr, --cdr`**
  The directory in the repository that contains the buildpacks file or the Dockerfile. The
  build context directory option is allowed only if the `--build-source` option is set. This
  value is optional.

  **`--build-dockerfile, --dockerfile, --bdf, --df`**
  The path to the Dockerfile. Specify this option only if the name is other than `Dockerfile`.
   The build dockerfile option is allowed only if the `--build-source` option is set. This
  value is optional. The default value is `Dockerfile`.

  **`--build-git-repo-secret, --git-repo-secret, --bgrs, --grs, --repo`**
  The name of the SSH secret, which contains the credentials to access the private repository
  that contains the source code to build your container image. To create this SSH secret, use
  the `secret create --format SSH` command. An SSH secret is also used as a Git repository
  access secret. This option is allowed only if the `--build-source` option is set to the URL
  of a Git repository. This value is optional.

  **`--build-size, --size, --bsz, --sz`**
  The size for the build, which determines the amount of resources used. Valid values are
  `small`, `medium`, `large`, `xlarge`, and `xxlarge`. For details, see Determining the size
  of the build. The build size option is allowed only if the `--build-source` option is set.
  This value is optional. The default value is `medium`.

  **`--build-strategy, --strategy, --bstr, --str`**
  The strategy to use for building the image. Valid values are `dockerfile` and `buildpacks`.
  The build strategy option is allowed only if the `--build-source` option is set. If not
  specified, the build strategy is determined by Code Engine if `--build-source` is specified
  and the source is on your local machine. This value is optional. The default value is
  `dockerfile`.

  **`--build-timeout, --bto`**
  The amount of time, in seconds, that can pass before the build must succeed or fail. The
  build timeout option is allowed only if the `--build-source` option is set. This value is
  optional. The default value is `600`.

  **Application Configuration Options**

  **`--argument, --arg, -a`**
  Set arguments for the application. Specify one argument per `--argument` option; for
  example, `-a argA -a argB`. This value overrides the default values that are specified
  within the container image. This value is optional.

  **`--command, --cmd, -c`**
  Set commands for the application. Specify one command per `--command` option; for example,
  `--cmd cmdA --cmd cmdB`. This value overrides the default command that is specified within
  the container image. This value is optional.

  **`--port, -p`**
  The port where the application listens. The format is `[NAME:]PORT`, where `[NAME:]` is
  optional. If `[NAME:]` is specified, valid values are `h2c`, or `http1`. When `[NAME:]` is
  not specified or is `http1`, the port uses HTTP/1.1. When `[NAME:]` is `h2c`, the port uses
  unencrypted HTTP/2. By default, Code Engine assumes apps listen for incoming connections on
  port 8080. If your application needs to listen on a port other than port 8080, use `--port`
  to specify the port. This value is optional.

  **`--user, -u`**
  The user ID (UID) that is used to run the application. This value overrides any user ID that
   is set in the application Dockerfile. The ID must conform to the operating system
  requirements of the container. This value is optional. The default value is `0`.

  **Resource Options**

  **`--cpu`**
  The amount of CPU set for the instance of the application. For valid values, see Supported
  memory and CPU combinations. This value is optional. The default value is `1`.

  **`--memory, -m`**
  The amount of memory set for the instance of the application. Use `M` for megabytes or `G`
  for gigabytes. For valid values, see Supported memory and CPU combinations. This value is
  optional. The default value is `4G`.

  **`--ephemeral-storage, --es`**
  The amount of ephemeral storage to set for the instance of the application. Use `M` for
  megabytes or `G` for gigabytes. This value is optional. The default value is `400M`.

  **Scaling Options**

  **`--concurrency, --cn`**
  The maximum number of requests that can be processed concurrently per instance. This value
  is optional. The default value is `100`.

  **`--concurrency-target, --ct`**
  The threshold of concurrent requests per instance at which one or more additional instances
  are created. Use this value to scale up instances based on concurrent number of requests. If
   `--concurrency-target` is not specified, this option defaults to the value of the
  `--concurrency` option. This value is optional. The default value is `0`.

  **`--max-scale, --max, --maxscale`**
  The maximum number of instances that can be used for this application. If you set this value
   to `0`, the application scales as needed. The application scaling is limited only by the
  instances per the resource quota for the project of your application. See Limits and quotas
  for Code Engine. This value is optional. The default value is `10`.

  **`--min-scale, --min, --minscale`**
  The minimum number of instances that can be used for this application. This option is useful
   to ensure that no instances are running when not needed. This value is optional. The
  default value is `0`.

  **`--scale-down-delay, --sdd`**
  The amount of time in seconds that must pass at reduced concurrency before the application
  is scaled down. An increase of the number of concurrent requests causes an application to
  scale up. If the number of requests drops (reduced concurrency), the specified amount of
  time for this option determines how long the reduced concurrency needs to persist, before
  the application is scaled down. By default, the application will be scaled down immediately,
   if reduced concurrency is detected. This value is optional. The default value is `0`.

  **Environment and Configuration Options**

  **`--env, -e`**
  Set environment variables in the application. Must be in `NAME=VALUE` format. This action
  adds a new environment variable or overrides an existing environment variable. Specify one
  environment variable per `--env` option; for example, `--env envA=A --env envB=B`. This
  value is optional.

  **`--env-cm, --env-from-configmap`**
  Set environment variables from the key-value pairs that are stored in this configmap by
  using one of the following ways:
  - To add environment variables for all keys in a configmap that is named `configmapName`,
  use the value `configmapName`. You can modify the environment variable names by specifying a
   prefix when referencing the configmap. To specify a prefix, use the value
  `PREFIX=CONFIGMAP_NAME`. Each resulting environment variable has the format
  `<PREFIX><NAME_OF_KEY_IN_CONFIGMAP>`. For example, to set the prefix for all variable names
  of keys in configmap `configmapName` to `CUSTOM_`, use the value `CUSTOM_=configmapName`. If
   the configmap `configmapName` contains `KEY_A`, the environment variable name is
  `CUSTOM_KEY_A`.
  - To add environment variables for individual keys, use the format `NAME:KEY_A,KEY_B`. For
  example, to add an environment variable for a single key `key1` in a configmap that is named
   `configmapName`, use the value `configmapName:key1`. To assign a different name to a
  referenced key, use the format `NAME:NEW_NAME=KEY_A`. For example, to add an environment
  variable named `myKey` for a single key `key1` in a configmap that is named `configmapName`,
   use the value `configmapName:myKey=key1`.

  This value is optional.

  **`--env-sec, --env-from-secret`**
  Set environment variables from the key-value pairs that are stored in a secret by using one
  of the following ways:
  - To add environment variables for all keys in a secret that is named `secretName`, use the
  value `secretName`. You can modify the environment variable names by specifying a prefix
  when referencing the secret. To specify a prefix, use the value `PREFIX=SECRET_NAME`. Each
  resulting environment variable has the format `<PREFIX><NAME_OF_KEY_IN_SECRET>`. For
  example, to set the prefix for all variable names of keys in secret `secretName` to
  `CUSTOM_`, use the value `CUSTOM_=secretName`. If the secret `secretName` contains `KEY_A`,
  the environment variable name is `CUSTOM_KEY_A`.
  - To add environment variables for individual keys, use the format `NAME:KEY_A,KEY_B`. For
  example, to add an environment variable for a single key `key1` in a secret that is named
  `secretName`, use the value `secretName:key1`. To assign a different name to a referenced
  key, use the format `NAME:NEW_NAME=KEY_A`. For example, to add an environment variable named
   `myKey` for a single key `key1` in a secret that is named `secretName`, use the value
  `secretName:myKey=key1`.

  This value is optional.

  **Mount Options**

  **`--mount-configmap, --mount-cm`**
  Add the contents of a configmap to the file system of your application container by
  providing a mount directory and the name of a configmap, with the format
  `MOUNT_DIRECTORY=CONFIGMAP_NAME`. Each mounted configmap must use a unique mount directory.
  For each key-value pair in the configmap, a file is added to the specified mount directory
  where the filename is the key and the contents of the file is the value of the key-value
  pair. Specify one mount configuration per `--mount-configmap` option; for example,
  `--mount-configmap /etc/config-a=config-a --mount-configmap /etc/config-b=config-b`. This
  value is optional.

  **`--mount-data-store, --mount-ds`**
  Mount a persistent data store. The format is `MOUNT_DIRECTORY=STORAGE_NAME[:SUBPATH]`. The
  `SUBPATH` is optional. This option can be specified multiple times. This value is optional.

  **`--mount-secret, --mount-sec`**
  Add the contents of a secret to the file system of your application container by providing a
   mount directory and the name of a secret, with the format `MOUNT_DIRECTORY=SECRET_NAME`.
  Each mounted secret must use a unique mount directory. For each key-value pair in the
  secret, a file is added to the specified mount directory where the filename is the key and
  the contents of the file is the value of the key-value pair. Specify one mount configuration
   per `--mount-secret` option; for example, `--mount-secret /etc/secret-a=secret--a
  --mount-secret /etc/secret-b=secret-b`. This value is optional.

  **Network and Visibility Options**

  **`--cluster-local, --cl`**
  Deploy the application with a project-only endpoint. Setting a project-only endpoint means
  that your app is not accessible from the public internet and network access is only possible
   from other Code Engine components that are running in the same project. This value is
  optional. The default value is `false`.

  **`--no-cluster-local, --ncl`**
  Deploy the application with a public endpoint. The application deploys such that it can
  receive requests from the public internet or from components within the Code Engine project.
   This value is optional. The default value is `true`.

  **`--visibility, -v`**
  The visibility for the application. Valid values are `public`, `private`, and `project`.
  Setting a visibility of `public` means that your app can receive requests from the public
  internet or from components within the Code Engine project. Setting a visibility of
  `private` means that your app is not accessible from the public internet and network access
  is only possible from other IBM Cloud using Virtual Private Endpoints (VPE) or Code Engine
  components that are running in the same project. Visibility can only be `private` if the
  project supports application private visibility. Setting a visibility of `project` means
  that your app is not accessible from the public internet and network access is only possible
   from other Code Engine components that are running in the same project. This value is
  optional.

  **Health Check Options**

  **`--probe-live, --pl`**
  Configure the liveness probe for this application in `NAME=VALUE` format. Valid options for
  `NAME` are: `type`, `port`, `path`, `interval`, `initial-delay`, `timeout`,
  `failure-threshold`. This option can be specified multiple times. The `type` property is
  required and valid values are `tcp` and `http`. For example, `--probe-live type=tcp
  --probe-live port=8080`. For more information about working with probes, see Configuring
  probes for your app. This value is optional.

  **`--probe-ready, --pr`**
  Configure the readiness probe for this application in `NAME=VALUE` format. Valid options for
   `NAME` are: `type`, `port`, `path`, `interval`, `initial-delay`, `timeout`,
  `failure-threshold`. This option can be specified multiple times. The `type` property is
  required and valid values are `tcp` and `http`. For example, `--probe-ready type=tcp
  --probe-ready port=8080`. For more information about working with probes, see Configuring
  probes for your app. This value is optional.

  **Timeout Options**

  **`--request-timeout, --rt, --timeout, -t`**
  The amount of time in seconds that can pass before requests made to the application must
  succeed or fail. This value is optional. The default value is `300`.

  **Security Options**

  **`--registry-secret, --rs`**
  The name of the registry secret. The registry secret is used to authenticate with a private
  registry when you download the container image. This value is optional.

  **`--service-account, --sa`**
  The name of the service account. A service account provides an identity for processes that
  run in an instance. For built-in service accounts, you can use the shortened names
  `manager`, `none`, `reader`, and `writer`. You can also use the full names that are prefixed
   with the Kubernetes Config Context, which can be determined with the `project current`
  command. This value is optional.

  **`--trusted-profiles-enabled, --trusted, --tpe`**
  Enable mounting of a compute resource token to the container of this application. This value
   is optional. The default value is `false`.

  **Execution Options**

  **`--force, -f`**
  Do not verify the existence of specified configmap and secret references. Configmap
  references are specified with the `--env-from-configmap` or `--mount-configmap` options.
  Secret references are specified with the `--env-from-secret`, `--mount-secret` or
  `--registry-secret` options. This value is optional. The default value is `false`.

  **`--no-wait, --nw`**
  Create the application and do not wait for the application to be ready. If you specify the
  `--no-wait` option, the application create begins and does not wait. Use the `app get`
  command to check the application status. This value is optional. The default value is
  `false`.

  **`--wait, -w`**
  Create the application and wait for the application to be ready. If you specify the `--wait`
   option, the application create waits for a maximum time in seconds, as set by the
  `--wait-timeout` option, for the application to become ready. If the application is not
  ready within the specified `--wait-timeout` period, the application create fails. This value
   is optional. The default value is `true`.

  **`--wait-timeout, --wto`**
  The length of time in seconds to wait for the application to be ready. This value is
  required if the `--wait` option is specified. This value is ignored if the `--no-wait`
  option is specified. The default value is `600`.

  **Output Options**

  **`--output, -o`**
  Specifies the format of the command output. Valid values are `json`, `yaml`,
  `jsonpath=JSONPATH_EXPRESSION`, `jsonpath-as-json=JSONPATH_EXPRESSION`, `url`, and
  `project-url`. Use `jsonpath` to specify the path to an element of the JSON output. This
  value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default
   value is `false`.

  **Revision Options**

  **`--rn, --revision-name`**
  The name of the revision. Use a name that is unique within the application.
  - The name can contain lowercase letters, numbers, and hyphens (`-`).
  - The name must end with a lowercase alphanumeric character.
  - The fully qualified revision name must be in the format, `Name_of_application-Name of
  revision`.
  - The fully qualified revision name must be 63 characters or fewer.

  This value is optional.

---

### `ibmcloud ce application delete`

  Delete an application.

  **Syntax**
```bash
  ibmcloud ce application delete --name APPLICATION_NAME [--force] [--ignore-not-found]
  [--no-wait] [--quiet] [--wait] [--wait-timeout WAIT_TIMEOUT]
```
  #### Command Options

  **Required Options**

  **`--name, -n`**
  The name of the application. This value is required.

  **Execution Options**

  **`--force, -f`**
  Force deletion without confirmation. This value is optional. The default value is `false`.

  **`--ignore-not-found, --inf`**
  If not found, do not fail. This value is optional. The default value is `false`.

  **Wait Options**

  **`--no-wait, --nw`**
  Delete the application and do not wait for the application to be deleted. If you specify the
   `--no-wait` option, the application delete begins and does not wait. Use the `app get`
  command to check the application status. This value is optional. The default value is
  `true`.

  **`--wait, -w`**
  Delete the application and wait for the application to be deleted. If you specify the
  `--wait` option, the application delete waits for a maximum time in seconds, as set by the
  `--wait-timeout` option, for the application to become deleted. If the application is not
  deleted within the specified `--wait-timeout` period, the application delete fails. This
  value is optional. The default value is `false`.

  **`--wait-timeout, --wto`**
  The length of time in seconds to wait for the application to be deleted. This value is
  required if the `--wait` option is specified. This value is ignored if the `--no-wait`
  option is specified. The default value is `600`.

  **Output Options**

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default
   value is `false`.

---

### `ibmcloud ce application events`

  Display the system events of application instances. System events are retained up to 60
  minutes.

  **Syntax**

```bash
  ibmcloud ce application events (--instance APP_INSTANCE | --application APP_NAME) [--output
  OUTPUT] [--quiet]
```

  #### Command Options

  **Required Options**

  **`--application, --app, -a, --name, -n`**
  Display the events of all the instances of the specified application. This value is required
   if `--instance` is not specified.

  **`--instance, -i`**
  The name of a specific application instance. Use the `app get` command to find the instance
  name. This value is required if `--application` is not specified.

  **Output Options**

  **`--output, -o`**
  Specifies the format of the command output. Valid values are `json`, `yaml`,
  `jsonpath=JSONPATH_EXPRESSION`, and `jsonpath-as-json=JSONPATH_EXPRESSION`. Use `jsonpath`
  to specify the path to an element of the JSON output. This value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default
   value is `false`.

---

### `ibmcloud ce application get`

  Display the details of an application.

  **Syntax**

  ```bash
  ibmcloud ce application get --name APPLICATION_NAME [--output OUTPUT] [--quiet] [--show-all-revisions]
  ```

  #### Command Options

  **Required Options**

  **`--name, -n`**
  The name of the application. This value is required.

  **Display Options**

  **`--show-all-revisions, -r`**
  Show all revisions for this application. If not specified, only revisions which are configured to receive traffic are shown. This value is optional. The default value is `false`.

  **Output Options**

  **`--output, -o`**
  Specifies the format of the command output. Valid values are `json`, `yaml`, `jsonpath=JSONPATH_EXPRESSION`, `jsonpath-as-json=JSONPATH_EXPRESSION`, `url`, and `project-url`. Use `jsonpath` to specify the path to an element of the JSON output. This value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default value is `false`.

---

### `ibmcloud ce application list`

  List all applications in a project.

  **Syntax**

  ```bash
  ibmcloud ce application list [--output OUTPUT] [--quiet] [--sort-by SORT_BY]
  ```

  #### Command Options

  **Display Options**

  **`--sort-by, -s`**
  Specifies the column by which to sort the list. Valid values are `name` and `age`. This value is optional. The default value is `name`.

  **Output Options**

  **`--output, -o`**
  Specifies the format of the command output. Valid values are `json`, `yaml`, `jsonpath=JSONPATH_EXPRESSION`, and `jsonpath-as-json=JSONPATH_EXPRESSION`. Use `jsonpath` to specify the path to an element of the JSON output. This value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default value is `false`.

---

### `ibmcloud ce application logs`

  Display the logs of application instances.

  **Syntax**

  ```bash
  ibmcloud ce application logs (--instance APP_INSTANCE | --application APP_NAME) [--all-containers] [--follow] [--output OUTPUT] [--quiet] [--raw] [--tail TAIL] [--timestamps]
  ```

  #### Command Options

  **Required Options**

  **`--application, --app, -a, --name, -n`**
  Display the logs of all the instances of the specified application. This value is required if `--instance` is not specified.

  **`--instance, -i`**
  The name of a specific application instance. Use the `app get` command to find the instance name. This value is required if `--application` is not specified.

  **Display Options**

  **`--all-containers, --all`**
  Display the logs of all containers of the specified application instances. This value is optional. The default value is `false`.

  **`--follow, -f`**
  Follow the logs of application instances. Use this option to stream logs of application instances. If you specify the `--follow` option, you must enter Ctrl+C to terminate this log command. This value is optional. The default value is `false`.

  **`--raw, -r`**
  Display logs without instance and container labels. This value is optional. The default value is `false`.

  **`--tail, -t`**
  Limit the display of logs of containers of the specified application instances to a maximum number of recent lines per container. For example, to display the last 3 lines of the logs of the containers of the specified application instances, specify `--tail 3`. If this option is not specified, all lines of the logs of the containers of the specified application instances are displayed. This value is optional. The default value is `-1`.

  **`--timestamps, --ts`**
  Include timestamps on each line in the log output. This value is optional. The default value is `false`.

  **Output Options**

  **`--output, -o`**
  Specifies the format of the command output. Valid values are `json`, `yaml`, `jsonpath=JSONPATH_EXPRESSION`, and `jsonpath-as-json=JSONPATH_EXPRESSION`. Use `jsonpath` to specify the path to an element of the JSON output. This value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default value is `false`.

---

### `ibmcloud ce application restart`

  Restart running application instances.

  **Syntax**

  ```bash
  ibmcloud ce application restart (--instance APP_INSTANCE | --application APP_NAME) [--quiet]
  ```

  #### Command Options

  **Required Options**

  **`--application, --app, -a, --name, -n`**
  Restart all the running instances of the specified application. This value is required if `--instance` is not specified.

  **`--instance, -i`**
  The name of a specific application instance. Use the `app get` command to find the instance name. This value is required if `--application` is not specified.

  **Output Options**

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default value is `false`.

---

### `ibmcloud ce application unbind`

  Unbind IBM Cloud service instances from an application.

  **Syntax**

  ```
  ibmcloud ce application unbind --name APP_NAME (--binding BINDING_NAME | --all) [--quiet]
  ```

  #### Command Options

  **Required Options**

  **`--name, -n`**
  The name of the application to unbind. This value is required.

  **`--binding, -b`**
  The name of the binding to unbind. Run `ibmcloud ce app get -n APP_NAME` to view binding names. This value is required if `--all` is not specified.

  **`--all, -A`**
  Unbinds all service instances for this application. This value is required if `--binding` is not specified. The default value is `false`.

  **Output Options**

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default value is `false`.

---

### `ibmcloud ce application update`

  Update an application. Updating your application creates a revision. When calls are made to the application, traffic is routed to the revision.

  **Syntax**

  ```bash
  ibmcloud ce application update --name APP_NAME [--argument ARGUMENT] [--arguments-clear] [--build-clear] [--build-commit BUILD_COMMIT] [--build-commit-clear] [--build-context-dir BUILD_CONTEXT_DIR] [--build-dockerfile BUILD_DOCKERFILE] [--build-git-repo-secret BUILD_GIT_REPO_SECRET] [--build-git-repo-secret-clear] [--build-size BUILD_SIZE] [--build-source BUILD_SOURCE] [--build-strategy BUILD_STRATEGY] [--build-timeout BUILD_TIMEOUT] [--cluster-local] [--command COMMAND] [--commands-clear] [--concurrency CONCURRENCY] [--concurrency-target CONCURRENCY_TARGET] [--cpu CPU] [--env ENV] [--env-from-configmap ENV_FROM_CONFIGMAP] [--env-from-configmap-rm ENV_FROM_CONFIGMAP_RM] [--env-from-secret ENV_FROM_SECRET] [--env-from-secret-rm ENV_FROM_SECRET_RM] [--env-rm ENV_RM] [--ephemeral-storage EPHEMERAL_STORAGE] [--force] [--image IMAGE] [--max-scale MAX_SCALE] [--memory MEMORY] [--min-scale MIN_SCALE] [--mount-configmap MOUNT_CONFIGMAP] [--mount-data-store MOUNT_DATA_STORE] [--mount-rm MOUNT_RM] [--mount-secret MOUNT_SECRET] [--no-cluster-local] [--no-wait] [--output OUTPUT] [--port PORT] [--probe-live PROBE_LIVE] [--probe-live-clear] [--probe-ready PROBE_READY] [--probe-ready-reset] [--quiet] [--rebuild] [--registry-secret REGISTRY_SECRET] [--registry-secret-clear] [--request-timeout REQUEST_TIMEOUT] [--revision-name REVISION_NAME] [--scale-down-delay SCALE_DOWN_DELAY] [--service-account SERVICE_ACCOUNT] [--service-account-clear] [--trusted-profiles-enabled] [--user USER] [--visibility VISIBILITY] [--wait] [--wait-timeout WAIT_TIMEOUT]
  ```

  #### Command Options

  **Required Options**

  **`--name, -n`**
  The name of the application. This value is required.

  **Image and Build Options**

  **`--image, -i`**
  The name of the image that is used for this application. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG` is not specified, the default is `latest`. This value is optional.

  **`--build-source, --source, --bsrc, --src`**
  The URL of the Git repository or the path to local source that contains your source code; for example `https://github.com/IBM/CodeEngine` or `.`. This value is optional.

  **`--build-clear, --bc`**
  Remove the association of a build from this application. The build clear option is allowed only if your app currently has an associated build. This value is optional. The default value is `false`.

  **`--build-commit, --commit, --bcm, --cm, --revision`**
  The commit, tag, or branch in the source repository to pull. The build commit option is allowed only if the `--build-source` option is set to the URL of a Git repository on this app update command, or your application currently has an associated build from a Git repository source. This value is optional.

  **`--build-commit-clear, --commit-clear, --bcmc, --cmc`**
  Clear the commit, tag, or branch in the source repository to pull. The commit clear option is allowed if your application currently has an associated build. This value is optional. The default value is `false`.

  **`--build-context-dir, --context-dir, --bcdr, --cdr`**
  The directory in the repository that contains the buildpacks file or the Dockerfile. The build context directory option is allowed if the `--build-source` option is set on this app update command, or your application currently has an associated build. This value is optional.

  **`--build-dockerfile, --dockerfile, --bdf, --df`**
  The path to the Dockerfile. Specify this option only if the name is other than `Dockerfile`. The build dockerfile option is allowed only if the `--build-source` option is set on this app update command, or your application currently has an associated build. This value is optional. The default value is `Dockerfile`.

  **`--build-git-repo-secret, --git-repo-secret, --bgrs, --grs, --repo`**
  The name of the SSH secret, which contains the credentials to access the private repository that contains the source code to build your container image. To create this SSH secret, use the `secret create --format SSH` command. An SSH secret is also used as a Git repository access secret. This option is allowed only if the `--build-source` option is set to the URL of a Git repository on this application update command, or your application currently has an associated build from a Git repository source. This value is optional.

  **`--build-git-repo-secret-clear, --git-repo-secret-clear, --bgrsc, --grsc`**
  Clear the SSH secret. This option is allowed if your application currently has an associated build. This value is optional. The default value is `false`.

  **`--build-size, --size, --bsz, --sz`**
  The size for the build, which determines the amount of resources used. Valid values are `small`, `medium`, `large`, `xlarge`, and `xxlarge`. For details, see Determining the size of the build. The build size option is allowed only if the `--build-source` option is set on this app update command, or your application currently has an associated build. This value is optional. The default value is `medium`.

  **`--build-strategy, --strategy, --bstr, --str`**
  The strategy to use for building the image. Valid values are `dockerfile` and `buildpacks`. The build strategy option is allowed only if the `--build-source` option is set on this app update command, or your application currently has an associated build. If not specified, the build strategy is determined by Code Engine if `--build-source` is specified and the source is on your local machine. This value is optional. The default value is `dockerfile`.

  **`--build-timeout, --bto`**
  The amount of time, in seconds, that can pass before the build must succeed or fail. The build timeout option is allowed only if the `--build-source` option is set on this app update command, or your application currently has an associated build. This value is optional. The default value is `600`.

  **`--rebuild`**
  Rebuild image from source. The rebuild option is allowed if your application currently has an associated build. This value is optional. The default value is `false`.

  **Application Configuration Options**

  **`--argument, --arg, -a`**
  Set arguments for the application. Specify one argument per `--argument` option; for example, `-a argA -a argB`. This value is optional.

  **`--arguments-clear, --ac`**
  Clear application arguments. This value is optional. The default value is `false`.

  **`--command, --cmd, -c`**
  Set commands for the application. Specify one command per `--command` option; for example, `--cmd cmdA --cmd cmdB`. This value overrides the default command that is specified within the container image. This value is optional.

  **`--commands-clear, --cc`**
  Clear application commands. This value is optional. The default value is `false`.

  **`--port, -p`**
  The port where the application listens. The format is `[NAME:]PORT`, where `[NAME:]` is optional. If `[NAME:]` is specified, valid values are `h2c`, or `http1`. When `[NAME:]` is not specified or is `http1`, the port uses HTTP/1.1. When `[NAME:]` is `h2c`, the port uses unencrypted HTTP/2. By default, Code Engine assumes apps listen for incoming connections on port 8080. If your application needs to listen on a port other than port 8080, use `--port` to specify the port. This value is optional.

  **`--user, -u`**
  The user ID (UID) that is used to run the application. This value overrides any user ID that is set in the application Dockerfile. The ID must conform to the operating system requirements of the container. This value is optional. The default value is `0`.

  **Resource Options**

  **`--cpu`**
  The amount of CPU set for the instance of the application. For valid values, see Supported memory and CPU combinations. This value is optional. The default value is `0`.

  **`--memory, -m`**
  The amount of memory set for the instance of the application. Use `M` for megabytes or `G` for gigabytes. For valid values, see Supported memory and CPU combinations. This value is optional.

  **`--ephemeral-storage, --es`**
  The amount of ephemeral storage to set for the instance of the application. Use `M` for megabytes or `G` for gigabytes. This value is optional.

  **Scaling Options**

  **`--concurrency, --cn`**
  The maximum number of requests that can be processed concurrently per instance. This value is optional. The default value is `0`.

  **`--concurrency-target, --ct`**
  The threshold of concurrent requests per instance at which one or more additional instances are created. Use this value to scale up instances based on concurrent number of requests. If `--concurrency-target` is not specified, this option defaults to the value of the `--concurrency` option. This value is optional. The default value is `0`.

  **`--max-scale, --max, --maxscale`**
  The maximum number of instances that can be used for this application. If you set this value to `0`, the application scales as needed. The application scaling is limited only by the instances per the resource quota for the project of your application. See Limits and quotas for Code Engine. This value is optional. The default value is `10`.

  **`--min-scale, --min, --minscale`**
  The minimum number of instances that can be used for this application. This value is optional. The default value is `0`.

  **`--scale-down-delay, --sdd`**
  The amount of time in seconds that must pass at reduced concurrency before the application is scaled down. An increase of the number of concurrent requests causes an application to scale up. If the number of requests drops (reduced concurrency), the specified amount of time for this option determines how long the reduced concurrency needs to persist, before the application is scaled down. By default, the application will be scaled down immediately, if reduced concurrency is detected. This value is optional. The default value is `0`.

  **Environment and Configuration Options**

  **`--env, -e`**
  Set environment variables in the application. Must be in `NAME=VALUE` format. This action adds a new environment variable or overrides an existing environment variable. Specify one environment variable per `--env` option; for example, `--env envA=A --env envB=B`. This value is optional.

  **`--env-cm, --env-from-configmap`**
  Set environment variables from the key-value pairs that are stored in this configmap by using one of the following ways:
  - To add environment variables for all keys in a configmap that is named `configmapName`, use the value `configmapName`. You can modify the environment variable names by specifying a prefix when referencing the configmap. To specify a prefix, use the value `PREFIX=CONFIGMAP_NAME`. Each resulting environment variable has the format `<PREFIX><NAME_OF_KEY_IN_CONFIGMAP>`. For example, to set the prefix for all variable names of keys in configmap `configmapName` to `CUSTOM_`, use the value `CUSTOM_=configmapName`. If the configmap `configmapName` contains `KEY_A`, the environment variable name is `CUSTOM_KEY_A`.
  - To add environment variables for individual keys, use the format `NAME:KEY_A,KEY_B`. For example, to add an environment variable for a single key `key1` in a configmap that is named `configmapName`, use the value `configmapName:key1`. To assign a different name to a referenced key, use the format `NAME:NEW_NAME=KEY_A`. For example, to add an environment variable named `myKey` for a single key `key1` in a configmap that is named `configmapName`, use the value `configmapName:myKey=key1`.

  This value is optional.

  **`--env-from-configmap-rm, --env-cm-rm`**
  Remove environment variable references to full configmaps by using the configmap name. To remove individual key references to configmaps, use the `--env-rm` option. This option can be specified multiple times. This value is optional.

  **`--env-sec, --env-from-secret`**
  Set environment variables from the key-value pairs that are stored in a secret by using one of the following ways:
  - To add environment variables for all keys in a secret that is named `secretName`, use the value `secretName`. You can modify the environment variable names by specifying a prefix when referencing the secret. To specify a prefix, use the value `PREFIX=SECRET_NAME`. Each resulting environment variable has the format `<PREFIX><NAME_OF_KEY_IN_SECRET>`. For example, to set the prefix for all variable names of keys in secret `secretName` to `CUSTOM_`, use the value `CUSTOM_=secretName`. If the secret `secretName` contains `KEY_A`, the environment variable name is `CUSTOM_KEY_A`.
  - To add environment variables for individual keys, use the format `NAME:KEY_A,KEY_B`. For example, to add an environment variable for a single key `key1` in a secret that is named `secretName`, use the value `secretName:key1`. To assign a different name to a referenced key, use the format `NAME:NEW_NAME=KEY_A`. For example, to add an environment variable named `myKey` for a single key `key1` in a secret that is named `secretName`, use the value `secretName:myKey=key1`.

  This value is optional.

  **`--env-from-secret-rm, --env-sec-rm`**
  Remove environment variable references to full secrets by using the secret name. To remove individual key references to secrets, use the `--env-rm` option. This option can be specified multiple times. This value is optional.

  **`--env-rm`**
  Remove environment variable references to the key of a key-value pair in a configmap or secret. To remove individual key references and literal values, specify the name of the key. This option can be specified multiple times. This value is optional.

  **Mount Options**

  **`--mount-configmap, --mount-cm`**
  Add the contents of a configmap to the file system of your application container by providing a mount directory and the name of a configmap, with the format `MOUNT_DIRECTORY=CONFIGMAP_NAME`. Each mounted configmap must use a unique mount directory. For each key-value pair in the configmap, a file is added to the specified mount directory where the filename is the key and the contents of the file is the value of the key-value pair. Specify one mount configuration per `--mount-configmap` option; for example, `--mount-configmap /etc/config-a=config-a --mount-configmap /etc/config-b=config-b`. This value is optional.

  **`--mount-data-store, --mount-ds`**
  Mount a persistent data store. The format is `MOUNT_DIRECTORY=STORAGE_NAME[:SUBPATH]`. The `SUBPATH` is optional. This option can be specified multiple times. This value is optional.

  **`--mount-secret, --mount-sec`**
  Add the contents of a secret to the file system of your application container by providing a mount directory and the name of a secret, with the format `MOUNT_DIRECTORY=SECRET_NAME`. Each mounted secret must use a unique mount directory. For each key-value pair in the secret, a file is added to the specified mount directory where the filename is the key and the contents of the file is the value of the key-value pair. Specify one mount configuration per `--mount-secret` option; for example, `--mount-secret /etc/secret-a=secret--a --mount-secret /etc/secret-b=secret-b`. This value is optional.

  **`--mount-rm`**
  Remove the contents of a configmap or secret from the file system of your application container by specifying the directory where the configmap or secret is mounted. Specify one mount directory per `--mount-rm` option; for example, `--mount-rm /etc/configmap-a --mount-rm /etc/secret-b`. This value is optional.

  **Network and Visibility Options**

  **`--cluster-local, --cl`**
  Deploy the application with a project-only endpoint. Setting a project-only endpoint means that your app is not accessible from the public internet and network access is only possible from other Code Engine components that are running in the same project. This value is optional. The default value is `false`.

  **`--no-cluster-local, --ncl`**
  Deploy the application with a public endpoint. The application deploys such that it can receive requests from the public internet or from components within the Code Engine project. This value is optional. The default value is `true`.

  **`--visibility, -v`**
  The visibility for the application. Valid values are `public`, `private`, and `project`. Setting a visibility of `public` means that your app can receive requests from the public internet or from components within the Code Engine project. Setting a visibility of `private` means that your app is not accessible from the public internet and network access is only possible from other IBM Cloud using Virtual Private Endpoints (VPE) or Code Engine components that are running in the same project. Visibility can only be `private` if the project supports application private visibility. Setting a visibility of `project` means that your app is not accessible from the public internet and network access is only possible from other Code Engine components that are running in the same project. This value is optional.

  **Health Check Options**

  **`--probe-live, --pl`**
  Configure the liveness probe for this application in `NAME=VALUE` format. Valid options for `NAME` are: `type`, `port`, `path`, `interval`, `initial-delay`, `timeout`, `failure-threshold`. This option can be specified multiple times. The `type` property is required and valid values are `tcp` and `http`. For example, `--probe-live type=tcp --probe-live port=8080`. For more information about working with probes, see Configuring probes for your app. This value is optional.

  **`--probe-live-clear, --plr`**
  Remove the liveness probe. This option is allowed only if your app currently has a liveness probe. This value is optional. The default value is `false`.

  **`--probe-ready, --pr`**
  Configure the readiness probe for this application in `NAME=VALUE` format. Valid options for `NAME` are: `type`, `port`, `path`, `interval`, `initial-delay`, `timeout`, `failure-threshold`. This option can be specified multiple times. The `type` property is required and valid values are `tcp` and `http`. For example, `--probe-ready type=tcp --probe-ready port=8080`. For more information about working with probes, see Configuring probes for your app. This value is optional.

  **`--probe-ready-reset, --prr`**
  Resets the readiness probe to the default configuration. This value is optional. The default value is `false`.

  **Timeout Options**

  **`--request-timeout, --rt, --timeout, -t`**
  The amount of time in seconds that can pass before requests made to the application must succeed or fail. This value is optional. The default value is `0`.

  **Security Options**

  **`--registry-secret, --rs`**
  The name of the registry secret. The registry secret is used to authenticate with a private registry when you download the container image. This value is optional.

  **`--registry-secret-clear, --rsc`**
  Clear the registry secret. This value is optional. The default value is `false`.

  **`--service-account, --sa`**
  The name of the service account. A service account provides an identity for processes that run in an instance. For built-in service accounts, you can use the shortened names `manager`, `none`, `reader`, and `writer`. You can also use the full names that are prefixed with the Kubernetes Config Context, which can be determined with the `project current` command. This value is optional.

  **`--service-account-clear, --sac`**
  Clear the service account. This value is optional. The default value is `false`.

  **`--trusted-profiles-enabled, --trusted, --tpe`**
  Enable mounting of a compute resource token to the container of this application. This value is optional. The default value is `false`.

  **Execution Options**

  **`--force, -f`**
  Do not verify the existence of specified configmap and secret references. Configmap references are specified with the `--env-from-configmap` or `--mount-configmap` options. Secret references are specified with the `--env-from-secret`, `--mount-secret` or `--registry-secret` options. This value is optional. The default value is `false`.

  **`--no-wait, --nw`**
  Update the application and do not wait for the application to be ready. If you specify the `--no-wait` option, the application update begins and does not wait. Use the `app get` command to check the application status. This value is optional. The default value is `false`.

  **`--wait, -w`**
  Update the application and wait for the application to be ready. If you specify the `--wait` option, the application update waits for a maximum time in seconds, as set by the `--wait-timeout` option, for the application to become ready. If the application is not ready within the specified `--wait-timeout` period, the application create fails. This value is optional. The default value is `true`.

  **`--wait-timeout, --wto`**
  The length of time in seconds to wait for the application to be updated. This value is required if the `--wait` option is specified. This value is ignored if the `--no-wait` option is specified. The default value is `600`.

  **Output Options**

  **`--output, -o`**
  Specifies the format of the command output. Valid values are `json`, `yaml`, `jsonpath=JSONPATH_EXPRESSION`, `jsonpath-as-json=JSONPATH_EXPRESSION`, `url`, and `project-url`. Use `jsonpath` to specify the path to an element of the JSON output. This value is optional.

  **`--quiet, -q`**
  Specify this option to reduce the output of the command. This value is optional. The default value is `false`.

  **Revision Options**

  **`--rn, --revision-name`**
  The name of the revision. Use a name that is unique within the application.
  - The name can contain lowercase letters, numbers, and hyphens (`-`).
  - The name must end with a lowercase alphanumeric character.
  - The fully qualified revision name must be in the format, `Name_of_application-Name of revision`.
  - The fully qualified revision name must be 63 characters or fewer.

  This value is optional.
