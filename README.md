## Floresta-ffi

This repository contains the code to generate ffi binding for [Floresta](https://github.com/Davidson-Souza/floresta). The code is generated using [uniffi](https://github.com/mozilla/uniffi-rs) and are curently tested on linux and MacOS, using Python 3. Uniffi supports other languages, but the code generation for those languages are not tested yet.

## How to generate the code

If you want to generate the bindings and use it, you can use the [just command runner](https://github.com/casey/just) to generate the code. The just command runner is a simple command runner that allows you to define commands in a file called `justfile`. The `justfile` in this repository contains the commands to generate the bindings for the supported languages. To generate the bindings, you need to run the following command:

```bash
just gen-<your-language>
```

Where `<your-language>` is the language you want to generate the bindings for. For example, to generate the bindings for python, you need to run the following command:

```bash
just gen-python
```

this will do two things: build the shared library and generate some glue code to use the shared library in python. The generated code will be in the `generated/<language>` folder, while the shared library will be in the `target/release` folder.

## Python example

To use it in Python, you need the generated bindings and the shared-object in the same folder. Then you can start `florestad` with

```python
from floresta import Florestad

daemon = Florestad()
daemon.start()

# do something

#at the end you need to stop the daemon

daemon.stop()
```

after you start it, you'll have a json-rpc server and an Electrum server running on the default ports, you may use them to communicate with the daemon, see your balance, send transactions, etc.

## Customizing the daemon

There's a `Config` object that may be passed to the `Florestad` constructor, it has the following fields:

- `cfilters`(bool) - Required: whether we should use BIP158 filters or not;
- `cfilter_types`(list(FilterType)) - Required: the types of filters we should use;
- `log_to_stdout`(bool) - Required: whether we should log to stdout or not;
- `network`(Network) - Optional: the network we should use, default is `Network::Bitcoin`;
- `data_dir`(str) - Optional: the directory where the daemon should store its data, default is `~/.floresta`;
- `wallet_xpub`(list(str)) - Optional: the xpubs of the wallets we should keep track of;
- `wallet_descriptor`(list(str)) - Optional: a list of output descriptors the wallets we should keep track of;
- `rescan`(int) - Optional: download and check if the blocks after this height have something to our wallet;
- `log_to_file`(bool);
- `assume_valid`(str) - Optional: we assume that all blocks before this have valid signatures;
- `config_file`(str) - Optional: path to a config file, default is inside the `datadir``;
- `proxy`(str) - Optional: a socks5 proxy to use for network connections;
- `connect`(str) - Optional: a node that we should connect exclusively to;
- `json_rpc_address`(str) - Optional: the address to bind the json-rpc server;
- `electrum_address`(str) - Optional: the address to bind the electrum server;

to set them, just create a `Config` object and pass it to the `Florestad` constructor, like this:

```python
from floresta import Florestad, Config, Network, FilterType

config = Config(
        cfilters=True,
        cfilter_types=[FilterType::All],
        log_to_stdout=True,
        network=Network::Bitcoin,
    )
daemon = Florestad(config)
daemon.start()
```