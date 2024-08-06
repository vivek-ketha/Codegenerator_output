import os
import urllib.request
import shutil

def download_file_from_url(url, destination):
    with urllib.request.urlopen(url) as response, open(destination, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

def main():
    base_directory = os.getcwd()
    maven_wrapper_properties_path = os.path.join(base_directory, ".mvn/wrapper/maven-wrapper.properties")
    maven_wrapper_jar_path = os.path.join(base_directory, ".mvn/wrapper/maven-wrapper.jar")
    url = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.0/maven-wrapper-0.4.0.jar"
    if os.path.exists(maven_wrapper_properties_path):
        with open(maven_wrapper_properties_path, "r") as properties_file:
            properties = dict(line.strip().split("=") for line in properties_file)
            if "wrapperUrl" in properties:
                url = properties["wrapperUrl"]
    if not os.path.exists(os.path.dirname(maven_wrapper_jar_path)):
        os.makedirs(os.path.dirname(maven_wrapper_jar_path))
    download_file_from_url(url, maven_wrapper_jar_path)

if __name__ == "__main__":
    main()