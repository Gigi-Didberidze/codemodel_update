from xml.dom import minidom
import json

mydoc = minidom.parse('function_test_suite.xml')
items = mydoc.getElementsByTagName('testsuite')
print("name: " + items[0].attributes['name'].value)
print("#tests: " + items[0].attributes['tests'].value)
print("#failures: " + items[0].attributes['failures'].value)
print("#errors: " + items[0].attributes['errors'].value)
print("time: " + items[0].attributes['time'].value)
print("#disabled: " + items[0].attributes['disabled'].value)

items_testcase = mydoc.getElementsByTagName('testcase')
for tcase in items_testcase:
    print(tcase.attributes['status'].value + " " + tcase.attributes['time'].value + " " + tcase.attributes['name'].value)

json_converted = {}
mydoc = minidom.parse('function_test_suite.xml')
items = mydoc.getElementsByTagName('testsuite')
items_testcase = mydoc.getElementsByTagName('testcase')

json_converted['test_suite'] = []
json_converted['test_suite'].append({
    'name': items[0].attributes['name'].value,
    '#tests': float(items[0].attributes['tests'].value),
    'failures': float(items[0].attributes['failures'].value),
    'errors': float(items[0].attributes['errors'].value),
    'time': float(items[0].attributes['time'].value),
    'disabled': float(items[0].attributes['disabled'].value),
})

json_converted['test_case'] = []
for i in items_testcase:
    json_converted['test_case'].append({
        'status': i.attributes['status'].value,
        'time': float(i.attributes['time'].value),
        'name': i.attributes['name'].value,
    })

with open('data_from_xml.json', 'w') as outfile:
    json.dump(json_converted, outfile)