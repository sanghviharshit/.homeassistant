# Combine multiple device trackers into one entity
# You can call the script using the following:
# - service: python_script.meta_device_tracker
#   data_template:
#     entity_id: '{{trigger.entity_id}}'

# OPTIONS
# List the trackers for each individual
RashmiTrackers = ['device_tracker.rashmisiphone', 'device_tracker.rashmiphone_rashmiphone',
                  'device_tracker.rashmiappiphone', 'device_tracker.sonu_sonu',
                  'device_tracker.e1594e53_21df_414c_82da_f655d5282fca']
AlokTrackers = ['device_tracker.myiphone', 'device_tracker.alokphone_alokphone',
                'device_tracker.alokiosiphone', 'device_tracker.alok_alok',
                'device_tracker.elantrase', 'device_tracker.b4445761_f6c0_4b7f_835f_cfdc03b47111']
# Get the entity that triggered the automation
triggeredEntity = data.get('entity_id')

# Set friendly name and the metatracker name based on the entity that triggered
if triggeredEntity in AlokTrackers:
    newFriendlyName = 'Alok Tracker'
    newEntityPicture = '/local/icons/Alok.png'
    metatrackerName = 'device_tracker.meta_alok'
elif triggeredEntity in RashmiTrackers:
    newFriendlyName = 'Rashmi Tracker'
    newEntityPicture = '/local/icons/Rashmi.png'
    metatrackerName = 'device_tracker.meta_rashmi'
else:
    newFriendlyName = None
    metatrackerName = None

# Get current & new state
newState = hass.states.get(triggeredEntity)
currentState = hass.states.get(metatrackerName)
# Get New data
newSource = newState.attributes.get('source_type')
newFriendlyName_temp = newState.attributes.get('friendly_name')

# If GPS source, set new coordinates
if newSource == 'gps':
    newLatitude = newState.attributes.get('latitude')
    newLongitude = newState.attributes.get('longitude')
    newgpsAccuracy = newState.attributes.get('gps_accuracy')
# If not, keep last known coordinates
elif newSource is not None and currentState.attributes.get('latitude') is not None:
    newLatitude = currentState.attributes.get('latitude')
    newLongitude = currentState.attributes.get('longitude')
    newgpsAccuracy = currentState.attributes.get('gps_accuracy')
# Otherwise return null
else:
    newLatitude = None
    newLongitude = None
    newgpsAccuracy = None

# Get Battery
if newState.attributes.get('battery') is not None:
    newBattery = newState.attributes.get('battery')
elif currentState is not None and currentState.attributes.get('battery') is not None:
    newBattery = currentState.attributes.get('battery')
else:
    newBattery = None

# Get velocity
if newState.attributes.get('velocity') is not None:
    newVelocity = newState.attributes.get('velocity')
elif currentState is not None and currentState.attributes.get('velocity') is not None:
    newVelocity = currentState.attributes.get('velocity')
else:
    newVelocity = None

if newState.state is not None:
    newStatus = newState.state
else:
    newStatus = currentState.state

# Create device_tracker.meta entity
hass.states.set(metatrackerName, newStatus, {
    'friendly_name': newFriendlyName,
    'entity_picture': newEntityPicture,
    'source_type': newSource,
    'battery': newBattery,
    'gps_accuracy': newgpsAccuracy,
    'latitude': newLatitude,
    'longitude': newLongitude,
    'velocity': newVelocity,
    'update_source': triggeredEntity,
    'show_last_changed': 'true'
})
