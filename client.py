def main():
    """"function that calls the API from
    flask_start server program.
    Gets json from /name, /name/<name>,
    and calculates distance between
    two points"""
    import requests
    import sys
    r2 = requests.get("http://vcm-3594.vm.duke.edu:5000/name")
    r2_json = r2.json()
    sys.stdout.write(str(r2_json))
    var_name = "KyleJanson"
    input_string = "http://vcm-3594.vm.duke.edu:5000/name/" + str(var_name)
    r3 = requests.get(input_string)
    r3_json = r3.json()
    sys.stdout.write(str(r3_json))
    r4 = requests.post("http://vcm-3594.vm.duke.edu:5000/distance",
                       json={"a": [2, 4], "b": [5, 6]})
    r4_json = r4.json()
    sys.stdout.write(str(r4_json))
if __name__ == "__main__":
    main()
