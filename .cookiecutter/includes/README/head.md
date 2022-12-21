```console
$ gha-token --app-id 123456 --installation-id 123456789 --private-key $PRIVATE_KEY
ghs_xyz***
```

`--app-id` is the App ID of your GitHub app.

`--installation-id` is the ID of an installation of your GitHub app.

`--private-key` is a private key belonging to your GitHub app.

Use an environment variable for `--private-key` to avoid revealing your app's private key.
