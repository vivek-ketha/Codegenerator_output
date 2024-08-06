from playwright.sync_api import sync_playwright

def download_maven_wrapper(base_directory):
    download_url = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.0/maven-wrapper-0.4.0.jar"
    wrapper_properties_path = ".mvn/wrapper/maven-wrapper.properties"
    wrapper_jar_path = ".mvn/wrapper/maven-wrapper.jar"
    wrapper_url_property = "wrapperUrl"

    maven_wrapper_properties = {}
    try:
        with open(os.path.join(base_directory, wrapper_properties_path), "r") as f:
            for line in f:
                if line.startswith(wrapper_url_property):
                    download_url = line.split("=")[1].strip()
                    break
    except FileNotFoundError:
        pass

    output_file = os.path.join(base_directory, wrapper_jar_path)
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    with open(output_file, "wb") as f:
        with urllib.request.urlopen(download_url) as response:
            f.write(response.read())

with sync_playwright() as p:
    download_maven_wrapper(p.executable_path)