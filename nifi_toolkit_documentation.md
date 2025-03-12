# Nifi Toolkit Help Documentation

## Table of Contents

- [demo quick-import](#demo-quick-import)
- [help](#help)
- [nifi add-asset-reference](#nifi-add-asset-reference)
- [nifi change-version-processor](#nifi-change-version-processor)
- [nifi cluster-summary](#nifi-cluster-summary)
- [nifi connect-node](#nifi-connect-node)
- [nifi create-asset](#nifi-create-asset)
- [nifi create-flow-analysis-rule](#nifi-create-flow-analysis-rule)
- [nifi create-param-context](#nifi-create-param-context)
- [nifi create-param-provider](#nifi-create-param-provider)
- [nifi create-reg-client](#nifi-create-reg-client)
- [nifi create-reporting-task](#nifi-create-reporting-task)
- [nifi create-service](#nifi-create-service)
- [nifi create-user-group](#nifi-create-user-group)
- [nifi create-user](#nifi-create-user)
- [nifi current-user](#nifi-current-user)
- [nifi delete-asset](#nifi-delete-asset)
- [nifi delete-flow-analysis-rule](#nifi-delete-flow-analysis-rule)
- [nifi delete-nar](#nifi-delete-nar)
- [nifi delete-node](#nifi-delete-node)
- [nifi delete-param-context](#nifi-delete-param-context)
- [nifi delete-param-provider](#nifi-delete-param-provider)
- [nifi delete-param](#nifi-delete-param)
- [nifi delete-reporting-task](#nifi-delete-reporting-task)
- [nifi disable-flow-analysis-rules](#nifi-disable-flow-analysis-rules)
- [nifi disable-services](#nifi-disable-services)
- [nifi disconnect-node](#nifi-disconnect-node)
- [nifi download-nar](#nifi-download-nar)
- [nifi enable-flow-analysis-rules](#nifi-enable-flow-analysis-rules)
- [nifi enable-services](#nifi-enable-services)
- [nifi export-param-context](#nifi-export-param-context)
- [nifi export-reporting-task](#nifi-export-reporting-task)
- [nifi export-reporting-tasks](#nifi-export-reporting-tasks)
- [nifi fetch-params](#nifi-fetch-params)
- [nifi get-access-token-spnego](#nifi-get-access-token-spnego)
- [nifi get-access-token](#nifi-get-access-token)
- [nifi get-asset](#nifi-get-asset)
- [nifi get-controller-configuration](#nifi-get-controller-configuration)
- [nifi get-flow-analysis-rule](#nifi-get-flow-analysis-rule)
- [nifi get-flow-analysis-rules](#nifi-get-flow-analysis-rules)
- [nifi get-node](#nifi-get-node)
- [nifi get-nodes](#nifi-get-nodes)
- [nifi get-param-context](#nifi-get-param-context)
- [nifi get-param-provider](#nifi-get-param-provider)
- [nifi get-policy](#nifi-get-policy)
- [nifi get-reg-client-id](#nifi-get-reg-client-id)
- [nifi get-reporting-task](#nifi-get-reporting-task)
- [nifi get-reporting-tasks](#nifi-get-reporting-tasks)
- [nifi get-root-id](#nifi-get-root-id)
- [nifi get-service](#nifi-get-service)
- [nifi get-services](#nifi-get-services)
- [nifi import-param-context](#nifi-import-param-context)
- [nifi import-reporting-tasks](#nifi-import-reporting-tasks)
- [nifi list-assets](#nifi-list-assets)
- [nifi list-branches](#nifi-list-branches)
- [nifi list-buckets](#nifi-list-buckets)
- [nifi list-flow-versions](#nifi-list-flow-versions)
- [nifi list-flows](#nifi-list-flows)
- [nifi list-nar-component-types](#nifi-list-nar-component-types)
- [nifi list-nars](#nifi-list-nars)
- [nifi list-param-contexts](#nifi-list-param-contexts)
- [nifi list-param-providers](#nifi-list-param-providers)
- [nifi list-reg-clients](#nifi-list-reg-clients)
- [nifi list-user-groups](#nifi-list-user-groups)
- [nifi list-users](#nifi-list-users)
- [nifi logout-access-token](#nifi-logout-access-token)
- [nifi merge-param-context](#nifi-merge-param-context)
- [nifi offload-node](#nifi-offload-node)
- [nifi pg-change-all-versions](#nifi-pg-change-all-versions)
- [nifi pg-change-version](#nifi-pg-change-version)
- [nifi pg-connect](#nifi-pg-connect)
- [nifi pg-create-service](#nifi-pg-create-service)
- [nifi pg-create](#nifi-pg-create)
- [nifi pg-delete](#nifi-pg-delete)
- [nifi pg-disable-services](#nifi-pg-disable-services)
- [nifi pg-empty-queues](#nifi-pg-empty-queues)
- [nifi pg-enable-services](#nifi-pg-enable-services)
- [nifi pg-export](#nifi-pg-export)
- [nifi pg-get-all-versions](#nifi-pg-get-all-versions)
- [nifi pg-get-param-context](#nifi-pg-get-param-context)
- [nifi pg-get-services](#nifi-pg-get-services)
- [nifi pg-get-version](#nifi-pg-get-version)
- [nifi pg-import](#nifi-pg-import)
- [nifi pg-list-processors](#nifi-pg-list-processors)
- [nifi pg-list](#nifi-pg-list)
- [nifi pg-replace](#nifi-pg-replace)
- [nifi pg-set-param-context](#nifi-pg-set-param-context)
- [nifi pg-start](#nifi-pg-start)
- [nifi pg-status](#nifi-pg-status)
- [nifi pg-stop-version-control](#nifi-pg-stop-version-control)
- [nifi pg-stop](#nifi-pg-stop)
- [nifi processor-clear-state](#nifi-processor-clear-state)
- [nifi processor-run-once](#nifi-processor-run-once)
- [nifi processor-start](#nifi-processor-start)
- [nifi remove-asset-reference](#nifi-remove-asset-reference)
- [nifi remove-inherited-param-contexts](#nifi-remove-inherited-param-contexts)
- [nifi set-inherited-param-contexts](#nifi-set-inherited-param-contexts)
- [nifi set-param-provider-property](#nifi-set-param-provider-property)
- [nifi set-param](#nifi-set-param)
- [nifi set-reg-client-property](#nifi-set-reg-client-property)
- [nifi start-reporting-tasks](#nifi-start-reporting-tasks)
- [nifi stop-reporting-tasks](#nifi-stop-reporting-tasks)
- [nifi update-controller-configuration](#nifi-update-controller-configuration)
- [nifi update-policy](#nifi-update-policy)
- [nifi update-reg-client](#nifi-update-reg-client)
- [nifi update-user-group](#nifi-update-user-group)
- [nifi upload-nar](#nifi-upload-nar)
- [registry create-bucket](#registry-create-bucket)
- [registry create-flow](#registry-create-flow)
- [registry create-user-group](#registry-create-user-group)
- [registry create-user](#registry-create-user)
- [registry current-user](#registry-current-user)
- [registry delete-bucket](#registry-delete-bucket)
- [registry delete-flow](#registry-delete-flow)
- [registry diff-flow-versions](#registry-diff-flow-versions)
- [registry download-bundle](#registry-download-bundle)
- [registry export-all-flows](#registry-export-all-flows)
- [registry export-flow-version](#registry-export-flow-version)
- [registry get-access-token-spnego](#registry-get-access-token-spnego)
- [registry get-access-token](#registry-get-access-token)
- [registry get-bundle-checksum](#registry-get-bundle-checksum)
- [registry get-policy](#registry-get-policy)
- [registry import-all-flows](#registry-import-all-flows)
- [registry import-flow-version](#registry-import-flow-version)
- [registry list-buckets](#registry-list-buckets)
- [registry list-bundle-artifacts](#registry-list-bundle-artifacts)
- [registry list-bundle-groups](#registry-list-bundle-groups)
- [registry list-bundle-versions](#registry-list-bundle-versions)
- [registry list-extension-tags](#registry-list-extension-tags)
- [registry list-extensions](#registry-list-extensions)
- [registry list-flow-versions](#registry-list-flow-versions)
- [registry list-flows](#registry-list-flows)
- [registry list-user-groups](#registry-list-user-groups)
- [registry list-users](#registry-list-users)
- [registry logout-access-token](#registry-logout-access-token)
- [registry sync-flow-versions](#registry-sync-flow-versions)
- [registry transfer-flow-version](#registry-transfer-flow-version)
- [registry update-bucket-policy](#registry-update-bucket-policy)
- [registry update-policy](#registry-update-policy)
- [registry update-user-group](#registry-update-user-group)
- [registry update-user](#registry-update-user)
- [registry upload-bundle](#registry-upload-bundle)
- [registry upload-bundles](#registry-upload-bundles)
- [session clear](#session-clear)
- [session get](#session-get)
- [session keys](#session-keys)
- [session remove](#session-remove)
- [session set](#session-set)
- [session show](#session-show)

## demo quick-import

```text
## demo quick-import

Imports a flow from a file or a public URL into a pre-defined bucket named
'Quick Import'. This command will create the bucket if it doesn't exist, and
will create a new flow for each execution. The flow will then be imported to the
given NiFi instance.

usage: quick-import
 -i,--input <arg>                     A local file to read as input contents, a
                                      directory to read files from or a public
                                      URL to fetch
 -nifiProps,--nifiProps <arg>         A properties file to load for NiFi config
 -nifiRegProps,--nifiRegProps <arg>   A properties file to load for NiFi
                                      Registry config
 -verbose,--verbose                   Indicates that verbose output should be
                                      provided


```

[Back to Table of Contents](#table-of-contents)

## help

```text
## help

commands:

	demo quick-import
	nifi current-user
	nifi cluster-summary
	nifi connect-node
	nifi delete-node
	nifi disconnect-node
	nifi get-root-id
	nifi get-node
	nifi get-nodes
	nifi offload-node
	nifi list-reg-clients
	nifi create-reg-client
	nifi update-reg-client
	nifi set-reg-client-property
	nifi get-reg-client-id
	nifi list-branches
	nifi list-buckets
	nifi list-flows
	nifi list-flow-versions
	nifi pg-import
	nifi pg-connect
	nifi pg-start
	nifi pg-stop
	nifi pg-create
	nifi pg-get-version
	nifi pg-stop-version-control
	nifi pg-change-version
	nifi pg-change-all-versions
	nifi pg-get-all-versions
	nifi pg-list
	nifi pg-status
	nifi pg-get-services
	nifi pg-create-service
	nifi pg-enable-services
	nifi pg-disable-services
	nifi pg-get-param-context
	nifi pg-set-param-context
	nifi pg-replace
	nifi pg-export
	nifi pg-empty-queues
	nifi pg-delete
	nifi pg-list-processors
	nifi get-services
	nifi get-service
	nifi create-service
	nifi enable-services
	nifi disable-services
	nifi get-reporting-tasks
	nifi get-reporting-task
	nifi create-reporting-task
	nifi delete-reporting-task
	nifi start-reporting-tasks
	nifi stop-reporting-tasks
	nifi export-reporting-tasks
	nifi export-reporting-task
	nifi import-reporting-tasks
	nifi create-flow-analysis-rule
	nifi get-flow-analysis-rules
	nifi get-flow-analysis-rule
	nifi enable-flow-analysis-rules
	nifi disable-flow-analysis-rules
	nifi delete-flow-analysis-rule
	nifi list-users
	nifi create-user
	nifi list-user-groups
	nifi create-user-group
	nifi update-user-group
	nifi get-policy
	nifi update-policy
	nifi list-param-contexts
	nifi get-param-context
	nifi create-param-context
	nifi delete-param-context
	nifi set-inherited-param-contexts
	nifi remove-inherited-param-contexts
	nifi set-param
	nifi delete-param
	nifi export-param-context
	nifi import-param-context
	nifi merge-param-context
	nifi list-param-providers
	nifi get-param-provider
	nifi create-param-provider
	nifi delete-param-provider
	nifi fetch-params
	nifi set-param-provider-property
	nifi get-access-token
	nifi get-access-token-spnego
	nifi logout-access-token
	nifi get-controller-configuration
	nifi update-controller-configuration
	nifi change-version-processor
	nifi processor-start
	nifi processor-run-once
	nifi processor-clear-state
	nifi upload-nar
	nifi download-nar
	nifi list-nars
	nifi list-nar-component-types
	nifi delete-nar
	nifi create-asset
	nifi list-assets
	nifi get-asset
	nifi delete-asset
	nifi add-asset-reference
	nifi remove-asset-reference
	registry current-user
	registry list-buckets
	registry create-bucket
	registry delete-bucket
	registry list-flows
	registry create-flow
	registry delete-flow
	registry list-flow-versions
	registry export-flow-version
	registry import-flow-version
	registry sync-flow-versions
	registry transfer-flow-version
	registry diff-flow-versions
	registry upload-bundle
	registry upload-bundles
	registry list-bundle-groups
	registry list-bundle-artifacts
	registry list-bundle-versions
	registry download-bundle
	registry get-bundle-checksum
	registry list-extension-tags
	registry list-extensions
	registry list-users
	registry create-user
	registry update-user
	registry list-user-groups
	registry create-user-group
	registry update-user-group
	registry get-policy
	registry update-policy
	registry update-bucket-policy
	registry get-access-token
	registry get-access-token-spnego
	registry logout-access-token
	registry export-all-flows
	registry import-all-flows
	session keys
	session show
	session get
	session set
	session remove
	session clear
	exit
	help


```

[Back to Table of Contents](#table-of-contents)

## nifi add-asset-reference

```text
## nifi add-asset-reference

Adds an asset reference to a parameter. The parameter will be created if it does
not already exist.

usage: add-asset-reference
 -aid,--assetId <arg>             The id of an asset which can be referenced
                                  from a parameter
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pd,--paramDescription <arg>     The description of the parameter
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pn,--paramName <arg>            The name of the parameter
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ut,--updateTimeout <arg>        Number of seconds after which a parameter
                                  context update will timeout (default: 60,
                                  maximum: 600)
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi change-version-processor

```text
## nifi change-version-processor

Recursively changes the version of the instances of the specified processor. If
the process group is specified, the changes will be scoped to that process group
and its childs ; if not specified the changes will recursively apply to the root
process group. If the source version is specified, only instances with this
version will be updated to the new version.

usage: change-version-processor
 -ar,--artifact <arg>              The artifact id of a bundle
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -cver,--current-version <arg>     The current version of the bundle
 -extname,--extension-name <arg>   The qualified name of the extension
 -gr,--group <arg>                 The group id of a bundle
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -pgid,--processGroupId <arg>      The id of a process group
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -ver,--version <arg>              The version of the bundle
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi cluster-summary

```text
## nifi cluster-summary

Returns information about the node's cluster summary. This provides a way to
test if the node is in the expected state.

usage: cluster-summary
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi connect-node

```text
## nifi connect-node

Connects a node to the NiFi cluster.

usage: connect-node
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nnid,--nifiNodeId <arg>         The ID of a node in the NiFi cluster
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-asset

```text
## nifi create-asset

Creates an asset in a given parameter context which can be referenced in a
parameter.

usage: create-asset
 -af,--assetFile <arg>            A file containing the asset content, must
                                  contain full path and filename
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-flow-analysis-rule

```text
## nifi create-flow-analysis-rule

Creates a flow analysis rule from a local file.

usage: create-flow-analysis-rule
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-param-context

```text
## nifi create-param-context

Creates a parameter context with the given name. After creating the parameter
context, parameters can be added using the set-param command.

usage: create-param-context
 -bap,--basicAuthPassword <arg>         The password for basic auth
 -bau,--basicAuthUsername <arg>         The username for basic auth
 -btk,--bearerToken <arg>               The bearer token to be passed in the
                                        Authorization header of a request
 -cto,--connectionTimeout <arg>         Timeout parameter for creating a
                                        connection to NiFi/Registry, specified
                                        in milliseconds
 -h,--help                              Help
 -kp,--keyPasswd <arg>                  The key password of the keystore being
                                        used
 -ks,--keystore <arg>                   A keystore to use for TLS/SSL
                                        connections
 -ksp,--keystorePasswd <arg>            The password of the keystore being used
 -kst,--keystoreType <arg>              The type of key store being used such as
                                        PKCS12
 -ot,--outputType <arg>                 The type of output to produce (json or
                                        simple)
 -p,--properties <arg>                  A properties file to load arguments
                                        from, command line values will override
                                        anything in the properties file, must
                                        contain full path to file
 -pcd,--paramContextDescription <arg>   The description of a parameter context
 -pcn,--paramContextName <arg>          The name of a parameter context
 -pe,--proxiedEntity <arg>              The identity of an entity to proxy
 -rto,--readTimeout <arg>               Timeout parameter for reading from
                                        NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>                 A truststore to use for TLS/SSL
                                        connections
 -tsp,--truststorePasswd <arg>          The password of the truststore being
                                        used
 -tst,--truststoreType <arg>            The type of trust store being used such
                                        as PKCS12
 -u,--baseUrl <arg>                     The URL to execute the command against
 -verbose,--verbose                     Indicates that verbose output should be
                                        provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-param-provider

```text
## nifi create-param-provider

Creates a parameter provider. After creating the parameter provider, its
properties can be configured using the set-param-provider-property command.

usage: create-param-provider
 -bap,--basicAuthPassword <arg>           The password for basic auth
 -bau,--basicAuthUsername <arg>           The username for basic auth
 -btk,--bearerToken <arg>                 The bearer token to be passed in the
                                          Authorization header of a request
 -cto,--connectionTimeout <arg>           Timeout parameter for creating a
                                          connection to NiFi/Registry, specified
                                          in milliseconds
 -h,--help                                Help
 -kp,--keyPasswd <arg>                    The key password of the keystore being
                                          used
 -ks,--keystore <arg>                     A keystore to use for TLS/SSL
                                          connections
 -ksp,--keystorePasswd <arg>              The password of the keystore being
                                          used
 -kst,--keystoreType <arg>                The type of key store being used such
                                          as PKCS12
 -ot,--outputType <arg>                   The type of output to produce (json or
                                          simple)
 -p,--properties <arg>                    A properties file to load arguments
                                          from, command line values will
                                          override anything in the properties
                                          file, must contain full path to file
 -pe,--proxiedEntity <arg>                The identity of an entity to proxy
 -ppaid,--paramProviderArtifactId <arg>   The bundle artifact ID of a parameter
                                          provider
 -ppgid,--paramProviderGroupId <arg>      The bundle group ID of a parameter
                                          provider
 -ppn,--paramProviderName <arg>           The name of a parameter provider
 -ppt,--paramProviderType <arg>           The type (fully qualified class name)
                                          of a parameter provider
 -ppv,--paramProviderVersion <arg>        The bundle version of a parameter
                                          provider
 -rto,--readTimeout <arg>                 Timeout parameter for reading from
                                          NiFi/Registry, specified in
                                          milliseconds
 -ts,--truststore <arg>                   A truststore to use for TLS/SSL
                                          connections
 -tsp,--truststorePasswd <arg>            The password of the truststore being
                                          used
 -tst,--truststoreType <arg>              The type of trust store being used
                                          such as PKCS12
 -u,--baseUrl <arg>                       The URL to execute the command against
 -verbose,--verbose                       Indicates that verbose output should
                                          be provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-reg-client

```text
## nifi create-reg-client

Creates a registry client using the provided information.

usage: create-reg-client
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rcd,--registryClientDesc <arg>   The description of the registry client
 -rcn,--registryClientName <arg>   The name of the registry client
 -rct,--registryClientType <arg>   The type of the registry client
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-reporting-task

```text
## nifi create-reporting-task

Creates a reporting task from a local file.

usage: create-reporting-task
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-service

```text
## nifi create-service

Creates a controller service for reporting tasks from a local file.

usage: create-service
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-user-group

```text
## nifi create-user-group

Creates new user group.

usage: create-user-group
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ugn,--userGroupName <arg>       The name of a user group
 -uil,--userIdList <arg>          The comma-separated user id list
 -unl,--userNameList <arg>        The comma-separated user name list
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi create-user

```text
## nifi create-user

Creates new user.

usage: create-user
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -un,--userName <arg>             The name of a user
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi current-user

```text
## nifi current-user

Returns information about the user accessing NiFi. This provides a way to test
if the CLI is accessing NiFi as the expected user.

usage: current-user
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-asset

```text
## nifi delete-asset

Deletes an asset from a given parameter context

usage: delete-asset
 -aid,--assetId <arg>             The id of an asset which can be referenced
                                  from a parameter
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-flow-analysis-rule

```text
## nifi delete-flow-analysis-rule

Delete a flow analysis rule.

usage: delete-flow-analysis-rule
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -far,--flowAnalysisRuleId <arg>   The id of a flow analysis rule
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-nar

```text
## nifi delete-nar

Deletes a NAR from the NAR Manager

usage: delete-nar
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -force,--force                   Indicates to force the operation
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nid,--narId <arg>
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-node

```text
## nifi delete-node

Deletes a node from the NiFi cluster.

usage: delete-node
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nnid,--nifiNodeId <arg>         The ID of a node in the NiFi cluster
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-param-context

```text
## nifi delete-param-context

Deletes a parameter context.

usage: delete-param-context
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-param-provider

```text
## nifi delete-param-provider

Deletes a parameter provider.

usage: delete-param-provider
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -ppid,--paramProviderId <arg>    The id of a parameter provider
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-param

```text
## nifi delete-param

Deletes a given parameter from the given parameter context.

usage: delete-param
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pn,--paramName <arg>            The name of the parameter
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi delete-reporting-task

```text
## nifi delete-reporting-task

Delete a reporting task.

usage: delete-reporting-task
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rt,--reportingTaskId <arg>      The id of a reporting task
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi disable-flow-analysis-rules

```text
## nifi disable-flow-analysis-rules

Attempts to disable one or all flow analysis rule(s). In stand-alone mode this
command will not produce all of the output seen in interactive mode unless the
--verbose argument is specified.

usage: disable-flow-analysis-rules
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -far,--flowAnalysisRuleId <arg>   The id of a flow analysis rule
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi disable-services

```text
## nifi disable-services

Disables all controller services for reporting tasks. Any services that are in
use by a running reporting task will fail to be disabled and will need to be
stopped first using stop-reporting-tasks. In stand-alone mode this command will
not produce all of the output seen in interactive mode unless the --verbose
argument is specified.

usage: disable-services
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cs,--controllerServiceId <arg>   The id of a controller service
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi disconnect-node

```text
## nifi disconnect-node

Disconnects a node from the NiFi cluster.

usage: disconnect-node
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nnid,--nifiNodeId <arg>         The ID of a node in the NiFi cluster
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi download-nar

```text
## nifi download-nar

Downloads a NAR from the NAR Manager

usage: download-nar
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nid,--narId <arg>
 -od,--outputDirectory <arg>      A directory to write output to
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi enable-flow-analysis-rules

```text
## nifi enable-flow-analysis-rules

Attempts to enable one or all flow analysis rule(s). In stand-alone mode this
command will not produce all of the output seen in interactive mode unless the
--verbose argument is specified.

usage: enable-flow-analysis-rules
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -far,--flowAnalysisRuleId <arg>   The id of a flow analysis rule
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi enable-services

```text
## nifi enable-services

Attempts to enable all controller services for reporting tasks. In stand-alone
mode this command will not produce all of the output seen in interactive mode
unless the --verbose argument is specified.

usage: enable-services
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cs,--controllerServiceId <arg>   The id of a controller service
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi export-param-context

```text
## nifi export-param-context

Exports a given parameter context to a json representation, with the option of
writing to a file.

usage: export-param-context
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -o,--outputFile <arg>            A file to write output to, must contain full
                                  path and filename
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi export-reporting-task

```text
## nifi export-reporting-task

Exports a snapshot of the specified reporting task and any management controller
services used by the reporting task.  The --outputFile can be used to export to
a file, otherwise the content will be written to terminal or standard out.

usage: export-reporting-task
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -o,--outputFile <arg>            A file to write output to, must contain full
                                  path and filename
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rt,--reportingTaskId <arg>      The id of a reporting task
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi export-reporting-tasks

```text
## nifi export-reporting-tasks

Exports a snapshot of all reporting tasks and any management controller services
used by the reporting tasks.  The --outputFile can be used to export to a file,
otherwise the content will be written to terminal or standard out.

usage: export-reporting-tasks
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -o,--outputFile <arg>            A file to write output to, must contain full
                                  path and filename
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi fetch-params

```text
## nifi fetch-params

Fetches the parameters of a parameter provider.  If indicated, also applies the
parameters to any referencing parameter contexts. When applying parameters, the
--inputSource (-i) option specifies the location of a JSON file containing a
parameterProviderParameterApplication entity, which allows detailed
configuration of the applied groups and parameters.  For a simpler approach,
this argument may be omitted, and all fetched groups will be mapped to parameter
contexts of the same names, creating new parameter contexts if needed.  To
select sensitive vs. non-sensitive parameters, the --sensitiveParamPattern
(-spp) can be used.  If this is not supplied, all fetched parameters will
default to sensitive.  Note that the --inputSource argument overrides any
parameter sensitivity specified in the --sensitiveParamPattern argument.

usage: fetch-params
 -ap,--applyParameters                If specified, the fetched parameters will
                                      also be applied to all referencing
                                      parameter contexts
 -bap,--basicAuthPassword <arg>       The password for basic auth
 -bau,--basicAuthUsername <arg>       The username for basic auth
 -btk,--bearerToken <arg>             The bearer token to be passed in the
                                      Authorization header of a request
 -cto,--connectionTimeout <arg>       Timeout parameter for creating a
                                      connection to NiFi/Registry, specified in
                                      milliseconds
 -h,--help                            Help
 -i,--input <arg>                     A local file to read as input contents, a
                                      directory to read files from or a public
                                      URL to fetch
 -kp,--keyPasswd <arg>                The key password of the keystore being
                                      used
 -ks,--keystore <arg>                 A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>          The password of the keystore being used
 -kst,--keystoreType <arg>            The type of key store being used such as
                                      PKCS12
 -ot,--outputType <arg>               The type of output to produce (json or
                                      simple)
 -p,--properties <arg>                A properties file to load arguments from,
                                      command line values will override anything
                                      in the properties file, must contain full
                                      path to file
 -pe,--proxiedEntity <arg>            The identity of an entity to proxy
 -ppid,--paramProviderId <arg>        The id of a parameter provider
 -rto,--readTimeout <arg>             Timeout parameter for reading from
                                      NiFi/Registry, specified in milliseconds
 -spp,--sensitiveParamPattern <arg>   A Regular Expression indicating the names
                                      of parameters that should be fetched as
                                      Sensitive.  If not specified, and
                                      --inputSource (-i) is not specified, all
                                      fetched parameters will be Sensitive.
 -ts,--truststore <arg>               A truststore to use for TLS/SSL
                                      connections
 -tsp,--truststorePasswd <arg>        The password of the truststore being used
 -tst,--truststoreType <arg>          The type of trust store being used such as
                                      PKCS12
 -u,--baseUrl <arg>                   The URL to execute the command against
 -verbose,--verbose                   Indicates that verbose output should be
                                      provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-access-token-spnego

```text
## nifi get-access-token-spnego

Authenticates to NiFi via SPNEGO and returns an access token for use on future
requests as the value of the bearerToken argument. If a keytab or password is
not specified, then the ticket cache will be used and it is assumed that a kinit
was done for the given principal outside of the CLI.

usage: get-access-token-spnego
 -bap,--basicAuthPassword <arg>     The password for basic auth
 -bau,--basicAuthUsername <arg>     The username for basic auth
 -btk,--bearerToken <arg>           The bearer token to be passed in the
                                    Authorization header of a request
 -cto,--connectionTimeout <arg>     Timeout parameter for creating a connection
                                    to NiFi/Registry, specified in milliseconds
 -h,--help                          Help
 -kp,--keyPasswd <arg>              The key password of the keystore being used
 -krbKt,--kerberosKeytab <arg>      The keytab for a kerberos principal
 -krbPr,--kerberosPrincipal <arg>   The kerberos principal
 -krbPw,--kerberosPassword <arg>    The password for a kerberos principal
 -ks,--keystore <arg>               A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>        The password of the keystore being used
 -kst,--keystoreType <arg>          The type of key store being used such as
                                    PKCS12
 -ot,--outputType <arg>             The type of output to produce (json or
                                    simple)
 -p,--properties <arg>              A properties file to load arguments from,
                                    command line values will override anything
                                    in the properties file, must contain full
                                    path to file
 -pe,--proxiedEntity <arg>          The identity of an entity to proxy
 -rto,--readTimeout <arg>           Timeout parameter for reading from
                                    NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>             A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>      The password of the truststore being used
 -tst,--truststoreType <arg>        The type of trust store being used such as
                                    PKCS12
 -u,--baseUrl <arg>                 The URL to execute the command against
 -verbose,--verbose                 Indicates that verbose output should be
                                    provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-access-token

```text
## nifi get-access-token

Authenticates to NiFi with the given username and password and returns an access
token for use on future requests as the value of the bearerToken argument

usage: get-access-token
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pwd,--password <arg>            The password for authentication when obtaining
                                  an access token
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -usr,--username <arg>            The username for authentication when obtaining
                                  an access token
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-asset

```text
## nifi get-asset

Retrieves the content of the given asset.

usage: get-asset
 -aid,--assetId <arg>             The id of an asset which can be referenced
                                  from a parameter
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -od,--outputDirectory <arg>      A directory to write output to
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-controller-configuration

```text
## nifi get-controller-configuration

Retrieves controller configuration.

usage: get-controller-configuration
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-flow-analysis-rule

```text
## nifi get-flow-analysis-rule

Retrieves a flow analysis rule.

usage: get-flow-analysis-rule
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -far,--flowAnalysisRuleId <arg>   The id of a flow analysis rule
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-flow-analysis-rules

```text
## nifi get-flow-analysis-rules

Retrieves the list of flow analysis rules.

usage: get-flow-analysis-rules
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-node

```text
## nifi get-node

Retrieves the status for a node in the NiFi cluster.

usage: get-node
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nnid,--nifiNodeId <arg>         The ID of a node in the NiFi cluster
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-nodes

```text
## nifi get-nodes

Retrieves statuses for the nodes of the NiFi cluster.

usage: get-nodes
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-param-context

```text
## nifi get-param-context

Retrieves a parameter context by id and lists each parameter and its value.

usage: get-param-context
 -bap,--basicAuthPassword <arg>         The password for basic auth
 -bau,--basicAuthUsername <arg>         The username for basic auth
 -btk,--bearerToken <arg>               The bearer token to be passed in the
                                        Authorization header of a request
 -cto,--connectionTimeout <arg>         Timeout parameter for creating a
                                        connection to NiFi/Registry, specified
                                        in milliseconds
 -h,--help                              Help
 -kp,--keyPasswd <arg>                  The key password of the keystore being
                                        used
 -ks,--keystore <arg>                   A keystore to use for TLS/SSL
                                        connections
 -ksp,--keystorePasswd <arg>            The password of the keystore being used
 -kst,--keystoreType <arg>              The type of key store being used such as
                                        PKCS12
 -ot,--outputType <arg>                 The type of output to produce (json or
                                        simple)
 -p,--properties <arg>                  A properties file to load arguments
                                        from, command line values will override
                                        anything in the properties file, must
                                        contain full path to file
 -pcid,--paramContextId <arg>           The id of a parameter context
 -pcin,--paramContextIncludeInherited   Indicates that all inherited parameters
                                        should be included
 -pe,--proxiedEntity <arg>              The identity of an entity to proxy
 -rto,--readTimeout <arg>               Timeout parameter for reading from
                                        NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>                 A truststore to use for TLS/SSL
                                        connections
 -tsp,--truststorePasswd <arg>          The password of the truststore being
                                        used
 -tst,--truststoreType <arg>            The type of trust store being used such
                                        as PKCS12
 -u,--baseUrl <arg>                     The URL to execute the command against
 -verbose,--verbose                     Indicates that verbose output should be
                                        provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-param-provider

```text
## nifi get-param-provider

Retrieves a parameter provider by id and lists each configured property and
value, as well as any fetched parameter names

usage: get-param-provider
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -ppid,--paramProviderId <arg>    The id of a parameter provider
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-policy

```text
## nifi get-policy

Retrieves the configuration for an access policy.

usage: get-policy
 -bap,--basicAuthPassword <arg>      The password for basic auth
 -bau,--basicAuthUsername <arg>      The username for basic auth
 -btk,--bearerToken <arg>            The bearer token to be passed in the
                                     Authorization header of a request
 -cto,--connectionTimeout <arg>      Timeout parameter for creating a connection
                                     to NiFi/Registry, specified in milliseconds
 -h,--help                           Help
 -kp,--keyPasswd <arg>               The key password of the keystore being used
 -ks,--keystore <arg>                A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>         The password of the keystore being used
 -kst,--keystoreType <arg>           The type of key store being used such as
                                     PKCS12
 -ot,--outputType <arg>              The type of output to produce (json or
                                     simple)
 -p,--properties <arg>               A properties file to load arguments from,
                                     command line values will override anything
                                     in the properties file, must contain full
                                     path to file
 -pe,--proxiedEntity <arg>           The identity of an entity to proxy
 -poa,--accessPolicyAction <arg>     The action of an access policy (read or
                                     write)
 -por,--accessPolicyResource <arg>   The resource of an access policy
 -rto,--readTimeout <arg>            Timeout parameter for reading from
                                     NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>              A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>       The password of the truststore being used
 -tst,--truststoreType <arg>         The type of trust store being used such as
                                     PKCS12
 -u,--baseUrl <arg>                  The URL to execute the command against
 -verbose,--verbose                  Indicates that verbose output should be
                                     provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-reg-client-id

```text
## nifi get-reg-client-id

Returns the id of the first registry client found with the given name.

usage: get-reg-client-id
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rcn,--registryClientName <arg>   The name of the registry client
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-reporting-task

```text
## nifi get-reporting-task

Retrieves the status for a reporting task.

usage: get-reporting-task
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rt,--reportingTaskId <arg>      The id of a reporting task
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-reporting-tasks

```text
## nifi get-reporting-tasks

Retrieves the list of reporting tasks.

usage: get-reporting-tasks
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-root-id

```text
## nifi get-root-id

Returns the id of the root process group of the given NiFi instance.

usage: get-root-id
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-service

```text
## nifi get-service

Retrieves the status for a controller service.

usage: get-service
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cs,--controllerServiceId <arg>   The id of a controller service
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi get-services

```text
## nifi get-services

Retrieves the list of controller services for the reporting tasks.

usage: get-services
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi import-param-context

```text
## nifi import-param-context

Imports a parameter context using the output from the export-param-context
command as the context to import. If the context name and context description
arguments are specified, they will override what is in the context json. All
inherited parameter contexts are expected to have been imported already,
otherwise the operation will fail.

usage: import-param-context
 -bap,--basicAuthPassword <arg>         The password for basic auth
 -bau,--basicAuthUsername <arg>         The username for basic auth
 -btk,--bearerToken <arg>               The bearer token to be passed in the
                                        Authorization header of a request
 -cto,--connectionTimeout <arg>         Timeout parameter for creating a
                                        connection to NiFi/Registry, specified
                                        in milliseconds
 -h,--help                              Help
 -i,--input <arg>                       A local file to read as input contents,
                                        a directory to read files from or a
                                        public URL to fetch
 -kp,--keyPasswd <arg>                  The key password of the keystore being
                                        used
 -ks,--keystore <arg>                   A keystore to use for TLS/SSL
                                        connections
 -ksp,--keystorePasswd <arg>            The password of the keystore being used
 -kst,--keystoreType <arg>              The type of key store being used such as
                                        PKCS12
 -ot,--outputType <arg>                 The type of output to produce (json or
                                        simple)
 -p,--properties <arg>                  A properties file to load arguments
                                        from, command line values will override
                                        anything in the properties file, must
                                        contain full path to file
 -pcd,--paramContextDescription <arg>   The description of a parameter context
 -pcn,--paramContextName <arg>          The name of a parameter context
 -pe,--proxiedEntity <arg>              The identity of an entity to proxy
 -rto,--readTimeout <arg>               Timeout parameter for reading from
                                        NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>                 A truststore to use for TLS/SSL
                                        connections
 -tsp,--truststorePasswd <arg>          The password of the truststore being
                                        used
 -tst,--truststoreType <arg>            The type of trust store being used such
                                        as PKCS12
 -u,--baseUrl <arg>                     The URL to execute the command against
 -verbose,--verbose                     Indicates that verbose output should be
                                        provided


```

[Back to Table of Contents](#table-of-contents)

## nifi import-reporting-tasks

```text
## nifi import-reporting-tasks

Imports the contents of a reporting task snapshot produced from
export-reporting-tasks or export-reporting-task.

usage: import-reporting-tasks
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-assets

```text
## nifi list-assets

Lists the assets in the given parameter context.

usage: list-assets
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-branches

```text
## nifi list-branches

Returns the list of branches seen by the specified registry client.

usage: list-branches
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rcid,--registryClientId <arg>   The id of a registry client
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-buckets

```text
## nifi list-buckets

Returns the list of branches seen by the specified registry client.

usage: list-buckets
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -fb,--flowBranch <arg>           A branch for the flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rcid,--registryClientId <arg>   The id of a registry client
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-flow-versions

```text
## nifi list-flow-versions

Returns the list of flow versions for a given flow in a given branch and bucket
seen by the specified registry client.

usage: list-flow-versions
 -b,--bucketIdentifier <arg>      A bucket identifier
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -fb,--flowBranch <arg>           A branch for the flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rcid,--registryClientId <arg>   The id of a registry client
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-flows

```text
## nifi list-flows

Returns the list of flows in a given branch and bucket seen by the specified
registry client.

usage: list-flows
 -b,--bucketIdentifier <arg>      A bucket identifier
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -fb,--flowBranch <arg>           A branch for the flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rcid,--registryClientId <arg>   The id of a registry client
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-nar-component-types

```text
## nifi list-nar-component-types

Lists the available component types for a given NAR in the NAR Manager

usage: list-nar-component-types
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nid,--narId <arg>
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-nars

```text
## nifi list-nars

Lists the NARs in the NAR Manager

usage: list-nars
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-param-contexts

```text
## nifi list-param-contexts

Lists the parameter contexts that the current user is authorized to retrieve.

PRODUCES BACK-REFERENCES

usage: list-param-contexts
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-param-providers

```text
## nifi list-param-providers

Lists the parameter providers that the current user is authorized to retrieve.

usage: list-param-providers
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-reg-clients

```text
## nifi list-reg-clients

Returns the registry clients defined in the given NiFi instance.

usage: list-reg-clients
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-user-groups

```text
## nifi list-user-groups

Retrieves the list of user group.

usage: list-user-groups
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi list-users

```text
## nifi list-users

Retrieves the list of user.

usage: list-users
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi logout-access-token

```text
## nifi logout-access-token

Performs a logout for the given access token

usage: logout-access-token
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi merge-param-context

```text
## nifi merge-param-context

Adds any parameters that exist in the exported context that don't exist in the
existing context.  Overwrites any existing inherited parameter contexts with the
provided list.

usage: merge-param-context
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi offload-node

```text
## nifi offload-node

Offloads a node of the NiFi cluster.

usage: offload-node
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nnid,--nifiNodeId <arg>         The ID of a node in the NiFi cluster
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-change-all-versions

```text
## nifi pg-change-all-versions

Changes the version for all of the controlled process group instances for a
given flow ID. This can be used to upgrade all the instances of a versioned flow
to a new version, or revert to a previous version. If no version is specified,
the latest version will be used. If no process group ID is provided, the root
process group will be used to recursively search for all instances of the Flow
ID. It is possible to force the recursive operation and not stop the operation
in case the upgrade of a process group fails.

PRODUCES BACK-REFERENCES

usage: pg-change-all-versions
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -force,--force                   Indicates to force the operation
 -fv,--flowVersion <arg>          A version of a flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-change-version

```text
## nifi pg-change-version

Changes the version for a version controlled process group. This can be used to
upgrade to a new version, or revert to a previous version. If no version is
specified, the latest version will be used.

usage: pg-change-version
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -fv,--flowVersion <arg>          A version of a flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-connect

```text
## nifi pg-connect

Connects the output port of the source process group to the input port of a
destination process group.

usage: pg-connect
 -bap,--basicAuthPassword <arg>              The password for basic auth
 -bau,--basicAuthUsername <arg>              The username for basic auth
 -btk,--bearerToken <arg>                    The bearer token to be passed in
                                             the Authorization header of a
                                             request
 -cto,--connectionTimeout <arg>              Timeout parameter for creating a
                                             connection to NiFi/Registry,
                                             specified in milliseconds
 -destInput,--destination-input-port <arg>   The name of the input port in the
                                             destination process group
 -destPg,--destination-pg <arg>              The ID of the destination process
                                             group
 -h,--help                                   Help
 -kp,--keyPasswd <arg>                       The key password of the keystore
                                             being used
 -ks,--keystore <arg>                        A keystore to use for TLS/SSL
                                             connections
 -ksp,--keystorePasswd <arg>                 The password of the keystore being
                                             used
 -kst,--keystoreType <arg>                   The type of key store being used
                                             such as PKCS12
 -ot,--outputType <arg>                      The type of output to produce (json
                                             or simple)
 -p,--properties <arg>                       A properties file to load arguments
                                             from, command line values will
                                             override anything in the properties
                                             file, must contain full path to
                                             file
 -pe,--proxiedEntity <arg>                   The identity of an entity to proxy
 -rto,--readTimeout <arg>                    Timeout parameter for reading from
                                             NiFi/Registry, specified in
                                             milliseconds
 -sourceOutput,--source-output-port <arg>    The name of the output port in the
                                             source process group
 -sourcePg,--source-pg <arg>                 The ID of the source process group
 -ts,--truststore <arg>                      A truststore to use for TLS/SSL
                                             connections
 -tsp,--truststorePasswd <arg>               The password of the truststore
                                             being used
 -tst,--truststoreType <arg>                 The type of trust store being used
                                             such as PKCS12
 -u,--baseUrl <arg>                          The URL to execute the command
                                             against
 -verbose,--verbose                          Indicates that verbose output
                                             should be provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-create-service

```text
## nifi pg-create-service

Creates the controller service for the given process group from the local file.

usage: pg-create-service
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-create

```text
## nifi pg-create

Creates a process group child of the root group.

usage: pg-create
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgn,--processGroupName <arg>    The name of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-delete

```text
## nifi pg-delete

Deletes the given process group. Deleting a process group requires, stopping all
Processors, disabling all Controller Services, and emptying all Queues.

usage: pg-delete
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-disable-services

```text
## nifi pg-disable-services

Disables the controller services in the given process group. Any services that
are in use by a running component will fail to be disabled and will need to be
stopped first using pg-stop.

usage: pg-disable-services
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-empty-queues

```text
## nifi pg-empty-queues

Empty all queues, recursively, in the specified Process Group. It is recommended
to first use pg-stop.

usage: pg-empty-queues
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-enable-services

```text
## nifi pg-enable-services

Attempts to enable all controller services in the given PG. In stand-alone mode
this command will not produce all of the output seen in interactive mode unless
the --verbose argument is specified.

usage: pg-enable-services
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-export

```text
## nifi pg-export

Exports a given process group to a json representation, with or without the
referenced services from outside the target group.

usage: pg-export
 -bap,--basicAuthPassword <arg>       The password for basic auth
 -bau,--basicAuthUsername <arg>       The username for basic auth
 -btk,--bearerToken <arg>             The bearer token to be passed in the
                                      Authorization header of a request
 -cto,--connectionTimeout <arg>       Timeout parameter for creating a
                                      connection to NiFi/Registry, specified in
                                      milliseconds
 -h,--help                            Help
 -irs,--include-referenced-services   Indicates that referenced services from
                                      outside the target group will be included.
 -kp,--keyPasswd <arg>                The key password of the keystore being
                                      used
 -ks,--keystore <arg>                 A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>          The password of the keystore being used
 -kst,--keystoreType <arg>            The type of key store being used such as
                                      PKCS12
 -o,--outputFile <arg>                A file to write output to, must contain
                                      full path and filename
 -ot,--outputType <arg>               The type of output to produce (json or
                                      simple)
 -p,--properties <arg>                A properties file to load arguments from,
                                      command line values will override anything
                                      in the properties file, must contain full
                                      path to file
 -pe,--proxiedEntity <arg>            The identity of an entity to proxy
 -pgid,--processGroupId <arg>         The id of a process group
 -rto,--readTimeout <arg>             Timeout parameter for reading from
                                      NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>               A truststore to use for TLS/SSL
                                      connections
 -tsp,--truststorePasswd <arg>        The password of the truststore being used
 -tst,--truststoreType <arg>          The type of trust store being used such as
                                      PKCS12
 -u,--baseUrl <arg>                   The URL to execute the command against
 -verbose,--verbose                   Indicates that verbose output should be
                                      provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-get-all-versions

```text
## nifi pg-get-all-versions

Returns all of the available versions for a version controlled process group.

usage: pg-get-all-versions
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-get-param-context

```text
## nifi pg-get-param-context

Gets the id of the parameter context that is bound to the given process group.

usage: pg-get-param-context
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-get-services

```text
## nifi pg-get-services

Retrieves the list of controller services for the given process group.

usage: pg-get-services
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-get-version

```text
## nifi pg-get-version

Returns the current version information for a version controlled process group.

usage: pg-get-version
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-import

```text
## nifi pg-import

Creates a new process group by importing a versioned flow from a registry. If no
process group id is specified, then the created process group will be placed in
the root group. If only one registry client exists in NiFi, then it does not
need to be specified and will be automatically selected. The x and y coordinates
for the position of the imported process group may be optionally specified. If
left blank, the position will automatically be selected to avoid overlapping
with existing process groups.

usage: pg-import
 -b,--bucketIdentifier <arg>                     A bucket identifier
 -bap,--basicAuthPassword <arg>                  The password for basic auth
 -bau,--basicAuthUsername <arg>                  The username for basic auth
 -btk,--bearerToken <arg>                        The bearer token to be passed
                                                 in the Authorization header of
                                                 a request
 -cto,--connectionTimeout <arg>                  Timeout parameter for creating
                                                 a connection to NiFi/Registry,
                                                 specified in milliseconds
 -f,--flowIdentifier <arg>                       A flow identifier
 -fb,--flowBranch <arg>                          A branch for the flow
 -fv,--flowVersion <arg>                         A version of a flow
 -h,--help                                       Help
 -i,--input <arg>                                A local file to read as input
                                                 contents, a directory to read
                                                 files from or a public URL to
                                                 fetch
 -kepc,--keep-existing-parameter-context <arg>   If false, only directly
                                                 associated Parameter Contexts
                                                 will be copied, inherited
                                                 Contexts with no direct
                                                 assignment to a Process Group
                                                 are ignored
 -kp,--keyPasswd <arg>                           The key password of the
                                                 keystore being used
 -ks,--keystore <arg>                            A keystore to use for TLS/SSL
                                                 connections
 -ksp,--keystorePasswd <arg>                     The password of the keystore
                                                 being used
 -kst,--keystoreType <arg>                       The type of key store being
                                                 used such as PKCS12
 -ot,--outputType <arg>                          The type of output to produce
                                                 (json or simple)
 -p,--properties <arg>                           A properties file to load
                                                 arguments from, command line
                                                 values will override anything
                                                 in the properties file, must
                                                 contain full path to file
 -pe,--proxiedEntity <arg>                       The identity of an entity to
                                                 proxy
 -pgid,--processGroupId <arg>                    The id of a process group
 -px,--posX <arg>                                The x coordinate of a position
 -py,--posY <arg>                                The y coordinate of a position
 -rcid,--registryClientId <arg>                  The id of a registry client
 -rto,--readTimeout <arg>                        Timeout parameter for reading
                                                 from NiFi/Registry, specified
                                                 in milliseconds
 -ts,--truststore <arg>                          A truststore to use for TLS/SSL
                                                 connections
 -tsp,--truststorePasswd <arg>                   The password of the truststore
                                                 being used
 -tst,--truststoreType <arg>                     The type of trust store being
                                                 used such as PKCS12
 -u,--baseUrl <arg>                              The URL to execute the command
                                                 against
 -verbose,--verbose                              Indicates that verbose output
                                                 should be provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-list-processors

```text
## nifi pg-list-processors

Returns the list of processors for the specified process group. Listing can be
scoped specific processors (source/destination)

usage: pg-list-processors
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -filter,--filter <arg>           Indicates a filter that should be used to
                                  perform the action
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-list

```text
## nifi pg-list

Returns the process groups contained in the specified process group. If no
process group is specified, then the root group will be used.

PRODUCES BACK-REFERENCES

usage: pg-list
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-replace

```text
## nifi pg-replace

Replaces the content of a process group with the content from the specified
versioned flow snapshot.

usage: pg-replace
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-set-param-context

```text
## nifi pg-set-param-context

Sets the parameter context bound to the given process group.

usage: pg-set-param-context
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-start

```text
## nifi pg-start

Starts the given process group which starts any enabled and valid components
contained in that group.

usage: pg-start
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-status

```text
## nifi pg-status

Returns the status of the specified process group.

usage: pg-status
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-stop-version-control

```text
## nifi pg-stop-version-control

Stops version control for the specified process group.

usage: pg-stop-version-control
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi pg-stop

```text
## nifi pg-stop

Stops the given process group which stops any running components in the given
group.

usage: pg-stop
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pgid,--processGroupId <arg>     The id of a process group
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi processor-clear-state

```text
## nifi processor-clear-state

Clears the state of a processor.

usage: processor-clear-state
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -procid,--processorId <arg>      The id of a processor
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi processor-run-once

```text
## nifi processor-run-once

Executes Run Once on a processor.

usage: processor-run-once
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -procid,--processorId <arg>      The id of a processor
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi processor-start

```text
## nifi processor-start

Starts a processor.

usage: processor-start
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -procid,--processorId <arg>      The id of a processor
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi remove-asset-reference

```text
## nifi remove-asset-reference

Removes an asset reference from a given parameter.

usage: remove-asset-reference
 -aid,--assetId <arg>             The id of an asset which can be referenced
                                  from a parameter
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pn,--paramName <arg>            The name of the parameter
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ut,--updateTimeout <arg>        Number of seconds after which a parameter
                                  context update will timeout (default: 60,
                                  maximum: 600)
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi remove-inherited-param-contexts

```text
## nifi remove-inherited-param-contexts

Removes all inherited parameter contexts from the given parameter context

usage: remove-inherited-param-contexts
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi set-inherited-param-contexts

```text
## nifi set-inherited-param-contexts

Sets a list of parameter context ids from which the given parameter context
should inherit parameters

usage: set-inherited-param-contexts
 -bap,--basicAuthPassword <arg>           The password for basic auth
 -bau,--basicAuthUsername <arg>           The username for basic auth
 -btk,--bearerToken <arg>                 The bearer token to be passed in the
                                          Authorization header of a request
 -cto,--connectionTimeout <arg>           Timeout parameter for creating a
                                          connection to NiFi/Registry, specified
                                          in milliseconds
 -h,--help                                Help
 -kp,--keyPasswd <arg>                    The key password of the keystore being
                                          used
 -ks,--keystore <arg>                     A keystore to use for TLS/SSL
                                          connections
 -ksp,--keystorePasswd <arg>              The password of the keystore being
                                          used
 -kst,--keystoreType <arg>                The type of key store being used such
                                          as PKCS12
 -ot,--outputType <arg>                   The type of output to produce (json or
                                          simple)
 -p,--properties <arg>                    A properties file to load arguments
                                          from, command line values will
                                          override anything in the properties
                                          file, must contain full path to file
 -pcid,--paramContextId <arg>             The id of a parameter context
 -pcii,--paramContextInheritedIds <arg>   A comma-separated list of parameter
                                          context IDs to inherit
 -pe,--proxiedEntity <arg>                The identity of an entity to proxy
 -rto,--readTimeout <arg>                 Timeout parameter for reading from
                                          NiFi/Registry, specified in
                                          milliseconds
 -ts,--truststore <arg>                   A truststore to use for TLS/SSL
                                          connections
 -tsp,--truststorePasswd <arg>            The password of the truststore being
                                          used
 -tst,--truststoreType <arg>              The type of trust store being used
                                          such as PKCS12
 -u,--baseUrl <arg>                       The URL to execute the command against
 -verbose,--verbose                       Indicates that verbose output should
                                          be provided


```

[Back to Table of Contents](#table-of-contents)

## nifi set-param-provider-property

```text
## nifi set-param-provider-property

Sets a property on a parameter provider.

usage: set-param-provider-property
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -ppid,--paramProviderId <arg>    The id of a parameter provider
 -prna,--propertyName <arg>       The name of a property
 -prva,--propertyValue <arg>      The value of a property
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi set-param

```text
## nifi set-param

Creates or updates a parameter in the given parameter context.

usage: set-param
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pcid,--paramContextId <arg>     The id of a parameter context
 -pd,--paramDescription <arg>     The description of the parameter
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pn,--paramName <arg>            The name of the parameter
 -ps,--paramSensitive <arg>       Whether or not the parameter is sensitive
                                  (true/false)
 -pv,--paramValue <arg>           The value of a parameter
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ut,--updateTimeout <arg>        Number of seconds after which a parameter
                                  context update will timeout (default: 60,
                                  maximum: 600)
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi set-reg-client-property

```text
## nifi set-reg-client-property

Sets a property on a registry client.

usage: set-reg-client-property
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -prna,--propertyName <arg>       The name of a property
 -prva,--propertyValue <arg>      The value of a property
 -rcid,--registryClientId <arg>   The id of a registry client
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi start-reporting-tasks

```text
## nifi start-reporting-tasks

Starts any enabled and valid reporting tasks.

usage: start-reporting-tasks
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rt,--reportingTaskId <arg>      The id of a reporting task
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi stop-reporting-tasks

```text
## nifi stop-reporting-tasks

Stops any running reporting tasks.

usage: stop-reporting-tasks
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rt,--reportingTaskId <arg>      The id of a reporting task
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi update-controller-configuration

```text
## nifi update-controller-configuration

Updates controller configuration from a local file.

usage: update-controller-configuration
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi update-policy

```text
## nifi update-policy

Updates the access policy for the given resource and action, or creates the
policy if it doesn't not exist. In stand-alone mode this command will not
produce all of the output seen in interactive mode unless the --verbose argument
is specified.

usage: update-policy
 -bap,--basicAuthPassword <arg>      The password for basic auth
 -bau,--basicAuthUsername <arg>      The username for basic auth
 -btk,--bearerToken <arg>            The bearer token to be passed in the
                                     Authorization header of a request
 -cto,--connectionTimeout <arg>      Timeout parameter for creating a connection
                                     to NiFi/Registry, specified in milliseconds
 -gil,--groupIdList <arg>            The comma-separated user group id list
 -gnl,--groupNameList <arg>          The comma-separated user group name list
 -h,--help                           Help
 -kp,--keyPasswd <arg>               The key password of the keystore being used
 -ks,--keystore <arg>                A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>         The password of the keystore being used
 -kst,--keystoreType <arg>           The type of key store being used such as
                                     PKCS12
 -ot,--outputType <arg>              The type of output to produce (json or
                                     simple)
 -owp,--overwritePolicy              Overwrite the user list and group list for
                                     the access policy
 -p,--properties <arg>               A properties file to load arguments from,
                                     command line values will override anything
                                     in the properties file, must contain full
                                     path to file
 -pe,--proxiedEntity <arg>           The identity of an entity to proxy
 -poa,--accessPolicyAction <arg>     The action of an access policy (read or
                                     write)
 -por,--accessPolicyResource <arg>   The resource of an access policy
 -rto,--readTimeout <arg>            Timeout parameter for reading from
                                     NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>              A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>       The password of the truststore being used
 -tst,--truststoreType <arg>         The type of trust store being used such as
                                     PKCS12
 -u,--baseUrl <arg>                  The URL to execute the command against
 -uil,--userIdList <arg>             The comma-separated user id list
 -unl,--userNameList <arg>           The comma-separated user name list
 -verbose,--verbose                  Indicates that verbose output should be
                                     provided


```

[Back to Table of Contents](#table-of-contents)

## nifi update-reg-client

```text
## nifi update-reg-client

Updates the given registry client with a new name or description.

usage: update-reg-client
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -rcd,--registryClientDesc <arg>   The description of the registry client
 -rcid,--registryClientId <arg>    The id of a registry client
 -rcn,--registryClientName <arg>   The name of the registry client
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## nifi update-user-group

```text
## nifi update-user-group

Updates a user group.

usage: update-user-group
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ugid,--userGroupId <arg>        The id of a user group
 -ugn,--userGroupName <arg>       The name of a user group
 -uil,--userIdList <arg>          The comma-separated user id list
 -unl,--userNameList <arg>        The comma-separated user name list
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## nifi upload-nar

```text
## nifi upload-nar

Uploads a NAR to the NAR Manager

usage: upload-nar
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -nar,--narFile <arg>             A NAR file to upload, must contain full path
                                  and filename
 -npt,--narProcessing <arg>       Number of seconds after which a parameter
                                  context update will timeout (default: 60,
                                  maximum: 600)
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry create-bucket

```text
## registry create-bucket

Creates a bucket using the given name and description.

usage: create-bucket
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -bd,--bucketDesc <arg>           A bucket description
 -bn,--bucketName <arg>           A bucket name
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry create-flow

```text
## registry create-flow

Creates a flow in the given bucket with the given name and description.

usage: create-flow
 -b,--bucketIdentifier <arg>      A bucket identifier
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -fd,--flowDesc <arg>             A flow description
 -fn,--flowName <arg>             A flow name
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry create-user-group

```text
## registry create-user-group

Creates user group

usage: create-user-group
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ugn,--userGroupName <arg>       The name of a user group
 -uil,--userIdList <arg>          The comma-separated user id list
 -unl,--userNameList <arg>        The comma-separated user name list
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry create-user

```text
## registry create-user

Creates a new user.

usage: create-user
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -un,--userName <arg>             The name of a user
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry current-user

```text
## registry current-user

Returns information about the user accessing NiFi Registry. This provides a way
to test if the CLI is accessing NiFi Registry as the expected user.

usage: current-user
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry delete-bucket

```text
## registry delete-bucket

Deletes the bucket with the given id. If the bucket contains any items then the
force option must be used.

usage: delete-bucket
 -b,--bucketIdentifier <arg>      A bucket identifier
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -force,--force                   Indicates to force the operation
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry delete-flow

```text
## registry delete-flow

Deletes a flow from the registry. If the flow has one or more versions then the
force option must be used.

usage: delete-flow
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -force,--force                   Indicates to force the operation
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry diff-flow-versions

```text
## registry diff-flow-versions

Shows the differences between two versions of a flow.

usage: diff-flow-versions
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -fv1,--flowVersion1 <arg>        A version of a flow
 -fv2,--flowVersion2 <arg>        A version of a flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry download-bundle

```text
## registry download-bundle

Downloads the binary content of the given version of the extension bundle.

usage: download-bundle
 -ar,--artifact <arg>             The artifact id of a bundle
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -bn,--bucketName <arg>           A bucket name
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -gr,--group <arg>                The group id of a bundle
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -od,--outputDirectory <arg>      A directory to write output to
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ver,--version <arg>             The version of the bundle
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry export-all-flows

```text
## registry export-all-flows

List all the buckets, for each bucket, list all the flows, for each flow, list
all versions and export each version.Versions will be saved in the provided
target directory.

usage: export-all-flows
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -od,--outputDirectory <arg>      A directory to write output to
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry export-flow-version

```text
## registry export-flow-version

Exports a specific version of a flow. The --outputFile can be used to export to
a file, otherwise the content will be written to terminal or standard out.

usage: export-flow-version
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -fv,--flowVersion <arg>          A version of a flow
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -o,--outputFile <arg>            A file to write output to, must contain full
                                  path and filename
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry get-access-token-spnego

```text
## registry get-access-token-spnego

Authenticates to NiFi Registry via SPNEGO and returns an access token for use on
future requests as the value of the bearerToken argument. If a keytab or
password is not specified, then the ticket cache will be used and it is assumed
that a kinit was done for the given principal outside of the CLI.

usage: get-access-token-spnego
 -bap,--basicAuthPassword <arg>     The password for basic auth
 -bau,--basicAuthUsername <arg>     The username for basic auth
 -btk,--bearerToken <arg>           The bearer token to be passed in the
                                    Authorization header of a request
 -cto,--connectionTimeout <arg>     Timeout parameter for creating a connection
                                    to NiFi/Registry, specified in milliseconds
 -h,--help                          Help
 -kp,--keyPasswd <arg>              The key password of the keystore being used
 -krbKt,--kerberosKeytab <arg>      The keytab for a kerberos principal
 -krbPr,--kerberosPrincipal <arg>   The kerberos principal
 -krbPw,--kerberosPassword <arg>    The password for a kerberos principal
 -ks,--keystore <arg>               A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>        The password of the keystore being used
 -kst,--keystoreType <arg>          The type of key store being used such as
                                    PKCS12
 -ot,--outputType <arg>             The type of output to produce (json or
                                    simple)
 -p,--properties <arg>              A properties file to load arguments from,
                                    command line values will override anything
                                    in the properties file, must contain full
                                    path to file
 -pe,--proxiedEntity <arg>          The identity of an entity to proxy
 -rto,--readTimeout <arg>           Timeout parameter for reading from
                                    NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>             A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>      The password of the truststore being used
 -tst,--truststoreType <arg>        The type of trust store being used such as
                                    PKCS12
 -u,--baseUrl <arg>                 The URL to execute the command against
 -verbose,--verbose                 Indicates that verbose output should be
                                    provided


```

[Back to Table of Contents](#table-of-contents)

## registry get-access-token

```text
## registry get-access-token

Authenticates to NiFi Registry with the given username and password and returns
an access token for use on future requests as the value of the bearerToken
argument

usage: get-access-token
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -pwd,--password <arg>            The password for authentication when obtaining
                                  an access token
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -usr,--username <arg>            The username for authentication when obtaining
                                  an access token
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry get-bundle-checksum

```text
## registry get-bundle-checksum

Retrieves the SHA-256 checksum for the given bundle.

usage: get-bundle-checksum
 -ar,--artifact <arg>             The artifact id of a bundle
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -bn,--bucketName <arg>           A bucket name
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -gr,--group <arg>                The group id of a bundle
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ver,--version <arg>             The version of the bundle
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry get-policy

```text
## registry get-policy

Retrieves the configuration for an access policy.

usage: get-policy
 -bap,--basicAuthPassword <arg>      The password for basic auth
 -bau,--basicAuthUsername <arg>      The username for basic auth
 -btk,--bearerToken <arg>            The bearer token to be passed in the
                                     Authorization header of a request
 -cto,--connectionTimeout <arg>      Timeout parameter for creating a connection
                                     to NiFi/Registry, specified in milliseconds
 -h,--help                           Help
 -kp,--keyPasswd <arg>               The key password of the keystore being used
 -ks,--keystore <arg>                A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>         The password of the keystore being used
 -kst,--keystoreType <arg>           The type of key store being used such as
                                     PKCS12
 -ot,--outputType <arg>              The type of output to produce (json or
                                     simple)
 -p,--properties <arg>               A properties file to load arguments from,
                                     command line values will override anything
                                     in the properties file, must contain full
                                     path to file
 -pe,--proxiedEntity <arg>           The identity of an entity to proxy
 -poa,--accessPolicyAction <arg>     The action of an access policy (read or
                                     write)
 -por,--accessPolicyResource <arg>   The resource of an access policy
 -rto,--readTimeout <arg>            Timeout parameter for reading from
                                     NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>              A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>       The password of the truststore being used
 -tst,--truststoreType <arg>         The type of trust store being used such as
                                     PKCS12
 -u,--baseUrl <arg>                  The URL to execute the command against
 -verbose,--verbose                  Indicates that verbose output should be
                                     provided


```

[Back to Table of Contents](#table-of-contents)

## registry import-all-flows

```text
## registry import-all-flows

From a provided directory as input, the directory content must be generated by
the export-all-flows command, based on the file contents, the corresponding
buckets, flows and flow versions will be created.If not configured otherwise,
already existing objects will be skipped.

usage: import-all-flows
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -se,--skipExisting               Indicates to skip an operation if target
                                  object exists
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry import-flow-version

```text
## registry import-flow-version

Imports a version of a flow from a local file, or a public URL. The imported
version automatically becomes the next version of the given flow.

usage: import-flow-version
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -h,--help                        Help
 -i,--input <arg>                 A local file to read as input contents, a
                                  directory to read files from or a public URL
                                  to fetch
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-buckets

```text
## registry list-buckets

Lists the buckets that the current user has access to.

PRODUCES BACK-REFERENCES

usage: list-buckets
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-bundle-artifacts

```text
## registry list-bundle-artifacts

List the bundle artifacts in the given bucket and group.

usage: list-bundle-artifacts
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -bn,--bucketName <arg>           A bucket name
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -gr,--group <arg>                The group id of a bundle
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-bundle-groups

```text
## registry list-bundle-groups

Lists the bundle groups in the bucket with the given name. If a bucket name
contains spaces, the argument must be wrapped in quotes.

usage: list-bundle-groups
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -bn,--bucketName <arg>           A bucket name
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-bundle-versions

```text
## registry list-bundle-versions

Lists the versions of the specified extension bundle.

usage: list-bundle-versions
 -ar,--artifact <arg>             The artifact id of a bundle
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -bn,--bucketName <arg>           A bucket name
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -gr,--group <arg>                The group id of a bundle
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-extension-tags

```text
## registry list-extension-tags

Lists the tag counts for all extensions located in buckets the current user is
authorized for.

usage: list-extension-tags
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-extensions

```text
## registry list-extensions

Lists info for extensions, optionally filtering by one or more tags. If
specifying tags, multiple tags can be specified with a comma-separated list, and
each tag will be OR'd together.

usage: list-extensions
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -et,--extensionType <arg>        The type of extension, one of 'PROCESSOR',
                                  'CONTROLLER_SERVICE', or 'REPORTING_TASK'.
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -tags,--tags <arg>               A comma separated list of one or more
                                  extension tags
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-flow-versions

```text
## registry list-flow-versions

Lists all of the flows for the given bucket.

usage: list-flow-versions
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>        A flow identifier
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-flows

```text
## registry list-flows

Lists all of the flows in the given bucket.

PRODUCES BACK-REFERENCES

usage: list-flows
 -b,--bucketIdentifier <arg>      A bucket identifier
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-user-groups

```text
## registry list-user-groups

Retrieves the list of user group.

usage: list-user-groups
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry list-users

```text
## registry list-users

Retrieves the list of user.

usage: list-users
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry logout-access-token

```text
## registry logout-access-token

Performs a logout for the given access token

usage: logout-access-token
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry sync-flow-versions

```text
## registry sync-flow-versions

Syncs the versions of a flow to another flow, which could be in a different
bucket or registry. This command assumes the intent is to maintain the exact
version history across the two flows. The list of versions from the source flow
will be compared to the destination flow, and any versions not present will be
added. If --sourceProps is not provided then the source registry will be assumed
to be the same as the destination registry.

usage: sync-flow-versions
 -bap,--basicAuthPassword <arg>     The password for basic auth
 -bau,--basicAuthUsername <arg>     The username for basic auth
 -btk,--bearerToken <arg>           The bearer token to be passed in the
                                    Authorization header of a request
 -cto,--connectionTimeout <arg>     Timeout parameter for creating a connection
                                    to NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>          A flow identifier
 -h,--help                          Help
 -kp,--keyPasswd <arg>              The key password of the keystore being used
 -ks,--keystore <arg>               A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>        The password of the keystore being used
 -kst,--keystoreType <arg>          The type of key store being used such as
                                    PKCS12
 -ot,--outputType <arg>             The type of output to produce (json or
                                    simple)
 -p,--properties <arg>              A properties file to load arguments from,
                                    command line values will override anything
                                    in the properties file, must contain full
                                    path to file
 -pe,--proxiedEntity <arg>          The identity of an entity to proxy
 -rto,--readTimeout <arg>           Timeout parameter for reading from
                                    NiFi/Registry, specified in milliseconds
 -sf,--sourceFlowIdentifier <arg>   A flow identifier from the source registry
 -sp,--sourceProps <arg>            A properties file to load for the source
 -ts,--truststore <arg>             A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>      The password of the truststore being used
 -tst,--truststoreType <arg>        The type of trust store being used such as
                                    PKCS12
 -u,--baseUrl <arg>                 The URL to execute the command against
 -verbose,--verbose                 Indicates that verbose output should be
                                    provided


```

[Back to Table of Contents](#table-of-contents)

## registry transfer-flow-version

```text
## registry transfer-flow-version

Transfers a version of a flow directly from one flow to another, without needing
to export/import. If --sourceProps is not specified, the source flow is assumed
to be in the same registry as the destination flow. If --sourceFlowVersion is
not specified, then the latest version will be transferred.

usage: transfer-flow-version
 -bap,--basicAuthPassword <arg>     The password for basic auth
 -bau,--basicAuthUsername <arg>     The username for basic auth
 -btk,--bearerToken <arg>           The bearer token to be passed in the
                                    Authorization header of a request
 -cto,--connectionTimeout <arg>     Timeout parameter for creating a connection
                                    to NiFi/Registry, specified in milliseconds
 -f,--flowIdentifier <arg>          A flow identifier
 -h,--help                          Help
 -kp,--keyPasswd <arg>              The key password of the keystore being used
 -ks,--keystore <arg>               A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>        The password of the keystore being used
 -kst,--keystoreType <arg>          The type of key store being used such as
                                    PKCS12
 -ot,--outputType <arg>             The type of output to produce (json or
                                    simple)
 -p,--properties <arg>              A properties file to load arguments from,
                                    command line values will override anything
                                    in the properties file, must contain full
                                    path to file
 -pe,--proxiedEntity <arg>          The identity of an entity to proxy
 -rto,--readTimeout <arg>           Timeout parameter for reading from
                                    NiFi/Registry, specified in milliseconds
 -sf,--sourceFlowIdentifier <arg>   A flow identifier from the source registry
 -sfv,--sourceFlowVersion <arg>     A version of a flow from the source registry
 -sp,--sourceProps <arg>            A properties file to load for the source
 -ts,--truststore <arg>             A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>      The password of the truststore being used
 -tst,--truststoreType <arg>        The type of trust store being used such as
                                    PKCS12
 -u,--baseUrl <arg>                 The URL to execute the command against
 -verbose,--verbose                 Indicates that verbose output should be
                                    provided


```

[Back to Table of Contents](#table-of-contents)

## registry update-bucket-policy

```text
## registry update-bucket-policy

Updates access policy of bucket, NOTE: Overwrites the users/user-groups in the
specified policy

usage: update-bucket-policy
 -b,--bucketIdentifier <arg>       A bucket identifier
 -bap,--basicAuthPassword <arg>    The password for basic auth
 -bau,--basicAuthUsername <arg>    The username for basic auth
 -bn,--bucketName <arg>            A bucket name
 -btk,--bearerToken <arg>          The bearer token to be passed in the
                                   Authorization header of a request
 -cto,--connectionTimeout <arg>    Timeout parameter for creating a connection
                                   to NiFi/Registry, specified in milliseconds
 -gil,--groupIdList <arg>          The comma-separated user group id list
 -gnl,--groupNameList <arg>        The comma-separated user group name list
 -h,--help                         Help
 -kp,--keyPasswd <arg>             The key password of the keystore being used
 -ks,--keystore <arg>              A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>       The password of the keystore being used
 -kst,--keystoreType <arg>         The type of key store being used such as
                                   PKCS12
 -ot,--outputType <arg>            The type of output to produce (json or
                                   simple)
 -p,--properties <arg>             A properties file to load arguments from,
                                   command line values will override anything in
                                   the properties file, must contain full path
                                   to file
 -pe,--proxiedEntity <arg>         The identity of an entity to proxy
 -poa,--accessPolicyAction <arg>   The action of an access policy (read or
                                   write)
 -rto,--readTimeout <arg>          Timeout parameter for reading from
                                   NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>            A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>     The password of the truststore being used
 -tst,--truststoreType <arg>       The type of trust store being used such as
                                   PKCS12
 -u,--baseUrl <arg>                The URL to execute the command against
 -uil,--userIdList <arg>           The comma-separated user id list
 -unl,--userNameList <arg>         The comma-separated user name list
 -verbose,--verbose                Indicates that verbose output should be
                                   provided


```

[Back to Table of Contents](#table-of-contents)

## registry update-policy

```text
## registry update-policy

Updates the access policy for the given resource and action, or creates the
policy if it doesn't exist. In stand-alone mode this command will not produce
all of the output seen in interactive mode unless the --verbose argument is
specified.

usage: update-policy
 -bap,--basicAuthPassword <arg>      The password for basic auth
 -bau,--basicAuthUsername <arg>      The username for basic auth
 -btk,--bearerToken <arg>            The bearer token to be passed in the
                                     Authorization header of a request
 -cto,--connectionTimeout <arg>      Timeout parameter for creating a connection
                                     to NiFi/Registry, specified in milliseconds
 -gil,--groupIdList <arg>            The comma-separated user group id list
 -gnl,--groupNameList <arg>          The comma-separated user group name list
 -h,--help                           Help
 -kp,--keyPasswd <arg>               The key password of the keystore being used
 -ks,--keystore <arg>                A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>         The password of the keystore being used
 -kst,--keystoreType <arg>           The type of key store being used such as
                                     PKCS12
 -ot,--outputType <arg>              The type of output to produce (json or
                                     simple)
 -owp,--overwritePolicy              Overwrite the user list and group list for
                                     the access policy
 -p,--properties <arg>               A properties file to load arguments from,
                                     command line values will override anything
                                     in the properties file, must contain full
                                     path to file
 -pe,--proxiedEntity <arg>           The identity of an entity to proxy
 -poa,--accessPolicyAction <arg>     The action of an access policy (read or
                                     write)
 -por,--accessPolicyResource <arg>   The resource of an access policy
 -rto,--readTimeout <arg>            Timeout parameter for reading from
                                     NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>              A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>       The password of the truststore being used
 -tst,--truststoreType <arg>         The type of trust store being used such as
                                     PKCS12
 -u,--baseUrl <arg>                  The URL to execute the command against
 -uil,--userIdList <arg>             The comma-separated user id list
 -unl,--userNameList <arg>           The comma-separated user name list
 -verbose,--verbose                  Indicates that verbose output should be
                                     provided


```

[Back to Table of Contents](#table-of-contents)

## registry update-user-group

```text
## registry update-user-group

Updates existing user group.

usage: update-user-group
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ugid,--userGroupId <arg>        The id of a user group
 -ugn,--userGroupName <arg>       The name of a user group
 -uil,--userIdList <arg>          The comma-separated user id list
 -unl,--userNameList <arg>        The comma-separated user name list
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry update-user

```text
## registry update-user

Updates an existing user.

usage: update-user
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -ui,--userIdentifier <arg>       The identifier of a user
 -un,--userName <arg>             The name of a user
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## registry upload-bundle

```text
## registry upload-bundle

Uploads an extension bundle binary to the specified bucket in the registry.

usage: upload-bundle
 -b,--bucketIdentifier <arg>        A bucket identifier
 -bap,--basicAuthPassword <arg>     The password for basic auth
 -bau,--basicAuthUsername <arg>     The username for basic auth
 -btk,--bearerToken <arg>           The bearer token to be passed in the
                                    Authorization header of a request
 -cto,--connectionTimeout <arg>     Timeout parameter for creating a connection
                                    to NiFi/Registry, specified in milliseconds
 -ebf,--extensionBundleFile <arg>   An extension bundle file, such as a NAR or
                                    MiNiFi CPP binary
 -ebt,--extensionBundleType <arg>   The type of extension bundle, either
                                    nifi-nar or minifi-cpp
 -h,--help                          Help
 -kp,--keyPasswd <arg>              The key password of the keystore being used
 -ks,--keystore <arg>               A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>        The password of the keystore being used
 -kst,--keystoreType <arg>          The type of key store being used such as
                                    PKCS12
 -ot,--outputType <arg>             The type of output to produce (json or
                                    simple)
 -p,--properties <arg>              A properties file to load arguments from,
                                    command line values will override anything
                                    in the properties file, must contain full
                                    path to file
 -pe,--proxiedEntity <arg>          The identity of an entity to proxy
 -rto,--readTimeout <arg>           Timeout parameter for reading from
                                    NiFi/Registry, specified in milliseconds
 -skipSha256,--skipSha256           Skips the client side calculation of the
                                    SHA-256 when uploading an extension bundle
 -ts,--truststore <arg>             A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>      The password of the truststore being used
 -tst,--truststoreType <arg>        The type of trust store being used such as
                                    PKCS12
 -u,--baseUrl <arg>                 The URL to execute the command against
 -verbose,--verbose                 Indicates that verbose output should be
                                    provided


```

[Back to Table of Contents](#table-of-contents)

## registry upload-bundles

```text
## registry upload-bundles

Performs a bulk upload of multiple bundles to the specified bucket in the
registry. This command will look for files in the specified directory, and if
recurse (-r) is specified then it will search child directories recursively. If
fileExtension is specified then it will only consider files that have the
specified extension, such as '.nar'

usage: upload-bundles
 -b,--bucketIdentifier <arg>        A bucket identifier
 -bap,--basicAuthPassword <arg>     The password for basic auth
 -bau,--basicAuthUsername <arg>     The username for basic auth
 -btk,--bearerToken <arg>           The bearer token to be passed in the
                                    Authorization header of a request
 -cto,--connectionTimeout <arg>     Timeout parameter for creating a connection
                                    to NiFi/Registry, specified in milliseconds
 -ebd,--extensionBundleDir <arg>    A directory where extension bundles are
                                    located
 -ebt,--extensionBundleType <arg>   The type of extension bundle, either
                                    nifi-nar or minifi-cpp
 -fe,--fileExtension <arg>          A file extension such as '.nar'
 -h,--help                          Help
 -kp,--keyPasswd <arg>              The key password of the keystore being used
 -ks,--keystore <arg>               A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>        The password of the keystore being used
 -kst,--keystoreType <arg>          The type of key store being used such as
                                    PKCS12
 -ot,--outputType <arg>             The type of output to produce (json or
                                    simple)
 -p,--properties <arg>              A properties file to load arguments from,
                                    command line values will override anything
                                    in the properties file, must contain full
                                    path to file
 -pe,--proxiedEntity <arg>          The identity of an entity to proxy
 -r,--recursive                     Indicates the command should perform the
                                    action recursively
 -rto,--readTimeout <arg>           Timeout parameter for reading from
                                    NiFi/Registry, specified in milliseconds
 -skipSha256,--skipSha256           Skips the client side calculation of the
                                    SHA-256 when uploading an extension bundle
 -ts,--truststore <arg>             A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>      The password of the truststore being used
 -tst,--truststoreType <arg>        The type of trust store being used such as
                                    PKCS12
 -u,--baseUrl <arg>                 The URL to execute the command against
 -verbose,--verbose                 Indicates that verbose output should be
                                    provided


```

[Back to Table of Contents](#table-of-contents)

## session clear

```text
## session clear

Clears all values in the session.

usage: clear
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## session get

```text
## session get

Returns the value of the given variable in the session.

usage: get
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## session keys

```text
## session keys

Returns the available variable names that can be set in the session.

usage: keys
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## session remove

```text
## session remove

Removes the given variable from the session.

usage: remove
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## session set

```text
## session set

Sets the given variable in the session. Use the 'keys' command to show the
variable names that are supported.

usage: set
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

## session show

```text
## session show

Returns all of the variables and values in the session.

usage: show
 -bap,--basicAuthPassword <arg>   The password for basic auth
 -bau,--basicAuthUsername <arg>   The username for basic auth
 -btk,--bearerToken <arg>         The bearer token to be passed in the
                                  Authorization header of a request
 -cto,--connectionTimeout <arg>   Timeout parameter for creating a connection to
                                  NiFi/Registry, specified in milliseconds
 -h,--help                        Help
 -kp,--keyPasswd <arg>            The key password of the keystore being used
 -ks,--keystore <arg>             A keystore to use for TLS/SSL connections
 -ksp,--keystorePasswd <arg>      The password of the keystore being used
 -kst,--keystoreType <arg>        The type of key store being used such as
                                  PKCS12
 -ot,--outputType <arg>           The type of output to produce (json or simple)
 -p,--properties <arg>            A properties file to load arguments from,
                                  command line values will override anything in
                                  the properties file, must contain full path to
                                  file
 -pe,--proxiedEntity <arg>        The identity of an entity to proxy
 -rto,--readTimeout <arg>         Timeout parameter for reading from
                                  NiFi/Registry, specified in milliseconds
 -ts,--truststore <arg>           A truststore to use for TLS/SSL connections
 -tsp,--truststorePasswd <arg>    The password of the truststore being used
 -tst,--truststoreType <arg>      The type of trust store being used such as
                                  PKCS12
 -u,--baseUrl <arg>               The URL to execute the command against
 -verbose,--verbose               Indicates that verbose output should be
                                  provided


```

[Back to Table of Contents](#table-of-contents)

