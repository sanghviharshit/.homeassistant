# My Home Assistant Configuration
[![Build Status](https://travis-ci.com/sanghviharshit/.homeassistant.svg?token=b2FVcjMqgZdj9LXTgUWp&branch=master)](https://travis-ci.com/sanghviharshit/.homeassistant)

My [homeassistant](https://www.home-assistant.io) configuration repository is heavily inspired by [CCOSTAN](https://github.com/CCOSTAN/Home-AssistantConfig)

> Home Assistant is open source home automation that puts local control and privacy first

# Integrations

This repository includes integrations for the following platforms.

- Smartthings, Alexa, IFTTT, MQTT, TTS (Text to speech), Google cast, Android TV, Samsung TV, Apple TV, Kodi, Harmony, Google, Google Maps, Google Calendar, Android IP Camera, DuckDNS, Mailgun, Life360, Personal Capital, iCloud, Dark Sky, WAQI (Air Quality Index), Pihole, AirVisual, Lifx, Hyperion, Vantage, Tuya, Speedtest, Travis, Twitter, Mint, Lyft, Uber, Sonos, Plex, Spotify, USCIS, Crime Reports

# Structure
It is structured in separate directories for automations, sensors, binary sensors, custom components, device trackers, input boolean/number/select, lights, scrips, switches, scenes and sound files.

- [Configuration](./configuration.yaml)
- [Automations](./automation)
- [Custom Components](./custom_components)
  - Mint Finance
  - Life360
  - Illuminance
  - Personal Capital
  - Sector Performance
  - Tuya
- [Lights](./lights)
- [Device Trackers](./device_tracker)
- [Packages](./packages)
  - Battery levels
  - Holiday
  - Alarm clock
  - Briefings
  - Process monitor
  - RSS Feed
  - Network
  - Geolocation
  - Arrivals
  - Last message
- [Python Scripts](./python_scripts)
- [Scripts](./script)
  - Dog bark
  - Doorbell
  - Emergency
  - Flash notification
  - Initialization
  - Light effects
  - Media
  - Color scenes
  - Notification engine
  - Play custom media
  - Play radio
  - Financial portfolio
  - Speech engine
  - Speech processing
  - Store and restore lights
  - Update tracker
- [Sensor](./sensor)
  - Crime Reports
  - Home Assistant Statistics
  - Mail
  - Plex
  - Remote
  - Spotify Advertisement
  - System
  - USCIS
  - Smartthings and Xiaomi temperature/humidity, motion, door/window contact, vibration, water leak
- [Shell scripts](./shell_scripts)
  - Alexa Remote Control
  - Git
  - Home assistant update
  - Homebridge
  - Jinja code
  - Log components
- [Sound Files](./sounds)
- [Lovelace Themes](./frontend.yaml)

# [Custom Components](./custom_components)

Custom components and Python scripts in this repo can be installed manually or by using [Custom Updater](https://github.com/custom-components/custom_updater).

### Custom Updater
[custom_components.json](./custom_components.json) provides the details Custom Updater needs. See [Custom Updater Installation](https://github.com/custom-components/custom_updater/wiki/Installation) to install it.

#### Setup
Add the following to your configuration:
```
custom_updater:
  track:
    - components
  component_urls:
    - https://raw.githubusercontent.com/sanghviharshit/.homeassistant/master/custom_components.json
```

##### Installing
To install one of these custom components, use the [`custom_updater.install`](https://github.com/custom-components/custom_updater/wiki/Services#install-element-cardcomponentpython_script) service with appropriate service data, such as:
```
{
  "element": "sensor.mint_finance"
}
```

## Mint
Custom component for [Mint Finance](https://www.mint.com/)

This currently only works in a non `HEADLESS` mode due to limitations of the dependency it uses.

Here is an example of a typical configuration:

```
sensor:
  - platform: mint_finance
    username: !secret mint_username
    password: !secret mint_password
    monitored_categories:
      - investment
      - bank
      - 'other property'
      - credit
    unit_of_measurement: USD
    account_currency_override:
      CAD: !secret mint_cad_account_list
      INR: !secret mint_cad_account_list
```
### Configuration variables
- **username**: Your mint account username
- **password**: Your mint account password
- **monitored_categories** (Optional): List of categories you'd like to monitor. Available options are investment, bank, other property, credit, mortgage, loan, real estate, vehicle and unclassified.
- **unit_of_measurement** (Optional): Default is `USD`.
- **account_currency_override** (Optional): Mint only supports one currency, so your accounts from multiple different currencies will report numeric value in same currency as is instead of performing any currency conversions. With this option, you can provide list of accounts you'd like to covert into default `unit_of_measurement`
- **exclude_accounts** (Optional): List of accounts you'd like to exclude. We exclude accounts which are not active always. This option allows excluding any additional accounts you don't want to see in home assistant.


# TODO:
- Dash buttons
- Embed https://www.windy.com/?43.643,-79.400,5 (Ref https://github.com/arsaboo/homeassistant-config)
- Canada weather
- Enercare graphs

[![Analytics](https://ga-beacon.appspot.com/UA-59542024-4/.homeassistant/)](https://github.com/igrigorik/ga-beacon)
