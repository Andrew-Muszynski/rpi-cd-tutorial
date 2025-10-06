import adafruit_dht
import board

# DHT11 sensor setup
try:
    dht_device = adafruit_dht.DHT11(board.D4)  # GPIO 4
    sensor_initialized = True
except Exception as e:
    sensor_initialized = False
    init_error = str(e)

def get_sensor_data():
    """Read temperature and humidity from DHT11"""
    
    # If sensor failed to initialize, return error
    if not sensor_initialized:
        return {
            'temperature': None,
            'humidity': None,
            'unit': 'C',
            'status': f'Sensor initialization failed: {init_error}'
        }
    
    # Try to read sensor data
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        
        # DHT sensors sometimes return None
        if temperature is None or humidity is None:
            return {
                'temperature': None,
                'humidity': None,
                'unit': 'C',
                'status': 'Sensor returned no data - try refreshing'
            }
        
        return {
            'temperature': temperature,
            'humidity': humidity,
            'unit': 'C',
            'status': 'success'
        }
        
    except RuntimeError as e:
        # DHT sensors often timeout - this is normal
        return {
            'temperature': None,
            'humidity': None,
            'unit': 'C',
            'status': f'Read timeout (normal for DHT11)'
        }
    except Exception as e:
        return {
            'temperature': None,
            'humidity': None,
            'unit': 'C',
            'status': f'Error: {str(e)}'
        }