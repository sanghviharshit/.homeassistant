# My Home Assistant Configuration
[![Build Status](https://travis-ci.com/sanghviharshit/.homeassistant.svg?token=b2FVcjMqgZdj9LXTgUWp&branch=master)](https://travis-ci.com/sanghviharshit/.homeassistant)

# Summary
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
  - Hyperion
  - Lifx
- [Device Trackers](./device_tracker)
- [Packages](./packages)
  - Pihole
  - Speedtest
  - Twitter
  - iOS
  - Battery levels
  - Holiday
  - Alarm clock
  - Finance
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
  - Sonos
  - Speech engine
  - Speech processing
  - Store and restore lights
  - Tweet
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
- [Shell scripts](./shell_scripts)
  - Alexa Remote Control
  - Git
  - Home assistant update
  - Homebridge
  - Jinja code
  - Log components
- [Sound Files](./sounds)
- [Lovelace Themes](./frontend.yaml)

# Integrations
- Alexa
- IFTTT
- MQTT
- TTS (Text to speech)
- Google cast
- Android TV
- Samsung TV
- Apple TV
- Kodi
- Harmony
- Google
- Google Maps
- Google Calendar
- Android IP Camera
- DuckDNS
- Mailgun
- Life360
- Personal Capital
- iCloud
- Dark Sky
- WAQI (Air Quality Index)
- Pihole
- AirVisual
- Lifx
- Hyperion
- Vantage
- Tuya
- Speedtest
- Travis
- Twitter
- Mint
- Lyft
- Uber
- Sonos
- Plex
- Spotify
- USCIS
- Crime Reports

# [Custom Components](./custom_components)

## Mint Finance (https://www.mint.com/)

### Installing & Updating Custom Components & Python Scripts
The custom components and Python scripts in this repo can be installed manually or by using [Custom Updater](https://github.com/custom-components/custom_updater).

#### Manual Installation
See instructions provided on custom component's or Python script's doc page.
#### Custom Updater
[custom_components.json](./custom_components.json) provides the details Custom Updater needs. See [Custom Updater Installation](https://github.com/custom-components/custom_updater/wiki/Installation) to install it.

##### Setup
Add the following to your configuration:
```
custom_updater:
  track:
    - components
  component_urls:
    - https://raw.githubusercontent.com/sanghviharshit/.homeassistant/master/custom_components.json
```

##### Installing
To install one of these custom components or Python scripts for the first time, use the [`custom_updater.install`](https://github.com/custom-components/custom_updater/wiki/Services#install-element-cardcomponentpython_script) service with appropriate service data, such as:
```
{
  "element": "sensor.mint"
}
```



# TODO:
- Crime alerts
- Dash buttons
- Install home assistant on parent's phones and add automations
- Embed https://www.windy.com/?43.643,-79.400,5 (Ref https://github.com/arsaboo/homeassistant-config)
- Canada weather
- Enercare graphs
