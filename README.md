## FLI Colour Filter Wheel daemon

`fli_filterwheeld` interfaces with and wraps a FLI colour filter wheel and exposes it via Pyro.

`filter` is a commandline utility for controlling the filter wheel.

### Configuration

Configuration is read from json files that are installed by default to `/etc/filterwheeld`.
A configuration file is specified when launching the server, and the `filter` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "warwick_filterwheel", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "filterwheeld@warwick", # The name to use when writing messages to the observatory log.
  "control_machines": ["WarwickTCS"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `rockit.common.IP`.
  "move_timeout": 10, # Maximum time to switch between two filters
  "filters": ["NONE", "B", "V", "R", "I"] # Filters installed in each slot
}

```
## Initial Installation

The automated packaging scripts will push 4 RPM packages to the observatory package repository:

| Package                        | Description                                                                        |
|--------------------------------|------------------------------------------------------------------------------------|
| rockit-filterwheel-fli-server  | Contains the `fli_filterwheeld` server and systemd service file.                   |
| rockit-filterwheel-fli-client  | Contains the `filter` commandline utility for controlling the filter wheel server. |
| python3-rockit-filterwheel-fli | Contains the python module with shared code.                                       |
| warwick-filterwheel-fli-data   | Contains the json configuration for the Windmill Hill Observatory telescope.       |

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now fli_filterwheeld@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart fli_filterwheeld@<config>
```

### Testing Locally

The camera server and client can be run directly from a git clone:
```
./fli_filterwheeld test.json
FILTERWHEELD_CONFIG_PATH=./warwick.json ./filter status
```
