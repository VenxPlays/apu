from flask import Flask, request, jsonify
import requests
import json
from urllib.parse import unquote

app = Flask(__name__)

# Your captured cookies
CAPTURED_COOKIES = {
    'wordpress_sec_0e7c25ea157a5cf8f8dc31b8193e3c54': 'randnwwo%7C1773164344%7CCIgL92ZiPhlIkbZeMyEZ3FivyBPsaosZJnquiEBKEaQ%7Ce5858746089bcc115a223f90da0963d9f9fd8e8c3f81ef6011feb349c452661b',
    '_ga': 'GA1.1.1193784604.1765884370',
    'tk_ai': '%2FmOj5V3JWufnWX%2FWQ3H%2BTuqy',
    'sellkit_contact_segmentation': '%7B%22browser_language%22%3A%22en-GB%22%2C%22user_device%22%3A%22desktop%22%2C%22ip%22%3A%22152.58.32.18%22%2C%22user_type%22%3A%22returning_visitor%22%2C%22url_query_string%22%3A%5B%22wordfence_lh%22%2C%22hid%22%2C%22r%22%5D%7D',
    '_gcl_au': '1.1.13000787.1765884369.1394299782.1771954735.1771954743',
    'wordpress_logged_in_0e7c25ea157a5cf8f8dc31b8193e3c54': 'randnwwo%7C1773164344%7CCIgL92ZiPhlIkbZeMyEZ3FivyBPsaosZJnquiEBKEaQ%7Cbf011866d1d95353ee322576d8037e5fc4247e644cdf41ad5a2c737e695260a9',
    'PHPSESSID': '30eb89eccc31f0afdfcca076c6051b56',
    'wfwaf-authcookie-dd39a51d578a90279599cfa30f391b79': '22469%7Cother%7Cread%7C01ab720bf15a40b2190009e133eb208f5199697fe7eb5b8930f6e48b29736cee',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2026-03-03%2006%3A35%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fgreendieselengineering.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2026-03-03%2006%3A35%3A10%7C%7C%7Cep%3Dhttps%3A%2F%2Fgreendieselengineering.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36',
    'tk_qs': '',
    '_ga_Z18P4TVV8Z': 'GS2.1.s1772521510$o12$g0$t1772521536$j34$l0$h0',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgreendieselengineering.com%2Fmy-account%2Fadd-payment-method%2F',
    '_uetsid': '51c2f28016cf11f1aacde34d2ba71f29',
    '_uetvid': '050f8320da7211f08b55c907ee8ed0ca',
}

# Your captured headers
CAPTURED_HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://greendieselengineering.com',
    'referer': 'https://greendieselengineering.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# Your captured data
CAPTURED_DATA = {
    'action': 'geot_ajax',
    'vars[ajax_url]': 'https://greendieselengineering.com/wp-admin/admin-ajax.php',
    'vars[ajax]': '1',
    'vars[pid]': '10',
    'vars[is_archive]': '',
    'vars[is_search]': '',
    'vars[is_singular]': '1',
    'vars[is_front_page]': '',
    'vars[is_category]': '',
    'vars[is_page]': '1',
    'vars[is_single]': '',
    'vars[disable_remove_on_singular]': '',
    'vars[is_builder]': '',
    'vars[has_geo_posts]': '1',
    'vars[dropdown_search]': '',
    'vars[dropdown_redirect]': '',
    'vars[elementor_popup]': '1',
    'vars[hide_class]': '',
    'vars[hide_override_class]': '',
    'vars[remove_class]': '',
    'vars[remove_override_class]': '',
    'vars[disable_console]': '',
    'vars[geoloc_enable]': 'by_ip',
    'vars[geoloc_force]': '',
    'vars[geoloc_fail]': 'Geolocation is not supported by this browser',
    'vars[geot_cookies_duration]': '999',
    'pid': '10',
    'referrer': 'https://greendieselengineering.com/my-account/add-payment-method/',
    'url': 'https://greendieselengineering.com/my-account/add-payment-method/',
    'query_string': '',
    'is_category': '',
    'is_archive': '',
    'is_front_page': '',
    'is_search': '',
    'browser_language': 'en-GB',
    'geot_debug': '',
    'geot_debug_iso': '',
    'geot_state': '',
    'geot_state_code': '',
    'geot_city': '',
    'geot_zip': '',
    'geot_lat': '',
    'geot_lng': '',
    'geot_redirects': '1',
    'geot_blockers': '1',
}

@app.route('/')
def home():
    return jsonify({
        'service': 'GreenDiesel Engineering API Tool',
        'status': 'running',
        'endpoints': {
            'execute_request': '/api/v1/execute',
            'get_cookies': '/api/v1/cookies',
            'get_headers': '/api/v1/headers',
            'get_data': '/api/v1/data',
            'custom_request': '/api/v1/custom'
        },
        'base_url': request.host_url
    })

@app.route('/api/v1/execute', methods=['GET', 'POST'])
def execute_captured_request():
    """Execute the exact captured request"""
    try:
        # Create session with cookies
        session = requests.Session()
        session.cookies.update(CAPTURED_COOKIES)
        session.headers.update(CAPTURED_HEADERS)
        
        # Make the request
        response = session.post(
            'https://greendieselengineering.com/wp-admin/admin-ajax.php',
            data=CAPTURED_DATA,
            timeout=30
        )
        
        # Try to parse as JSON
        try:
            result = response.json()
        except:
            result = response.text
            
        return jsonify({
            'success': True,
            'status_code': response.status_code,
            'response': result,
            'cookies_used': list(CAPTURED_COOKIES.keys()),
            'endpoint': 'https://greendieselengineering.com/wp-admin/admin-ajax.php'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/v1/cookies', methods=['GET'])
def get_cookies():
    """Return the captured cookies (decoded)"""
    decoded = {}
    for key, value in CAPTURED_COOKIES.items():
        try:
            decoded[key] = unquote(value)
        except:
            decoded[key] = value
    
    return jsonify({
        'cookies_raw': CAPTURED_COOKIES,
        'cookies_decoded': decoded,
        'count': len(CAPTURED_COOKIES)
    })

@app.route('/api/v1/headers', methods=['GET'])
def get_headers():
    """Return the captured headers"""
    return jsonify({
        'headers': CAPTURED_HEADERS,
        'count': len(CAPTURED_HEADERS)
    })

@app.route('/api/v1/data', methods=['GET'])
def get_data():
    """Return the captured POST data"""
    return jsonify({
        'post_data': CAPTURED_DATA,
        'count': len(CAPTURED_DATA)
    })

@app.route('/api/v1/custom', methods=['POST'])
def custom_request():
    """Make a custom request using the captured session"""
    try:
        data = request.json
        
        if not data or 'endpoint' not in data:
            return jsonify({'error': 'Missing endpoint'}), 400
        
        session = requests.Session()
        session.cookies.update(CAPTURED_COOKIES)
        session.headers.update(CAPTURED_HEADERS)
        
        method = data.get('method', 'POST').upper()
        endpoint = data['endpoint']
        post_data = data.get('data', {})
        
        if method == 'POST':
            response = session.post(endpoint, data=post_data, timeout=30)
        elif method == 'GET':
            response = session.get(endpoint, params=post_data, timeout=30)
        else:
            return jsonify({'error': 'Method not supported'}), 400
        
        try:
            result = response.json()
        except:
            result = response.text
            
        return jsonify({
            'success': True,
            'status_code': response.status_code,
            'response': result,
            'method': method,
            'endpoint': endpoint
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/v1/session-info', methods=['GET'])
def session_info():
    """Get information about the captured session"""
    return jsonify({
        'domain': 'greendieselengineering.com',
        'logged_in': bool('wordpress_logged_in' in str(CAPTURED_COOKIES.keys())),
        'cookie_count': len(CAPTURED_COOKIES),
        'wordpress_session': 'PHPSESSID' in CAPTURED_COOKIES,
        'has_waf': 'wfwaf-authcookie' in str(CAPTURED_COOKIES.keys()),
        'user_agent': CAPTURED_HEADERS.get('user-agent', 'Unknown')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
