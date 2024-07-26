
import os
import urllib.request

def download_file_from_url(url, destination_path):
    with urllib.request.urlopen(url) as response, open(destination_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)

def main():
    base_directory = os.getcwd()
    maven_wrapper_properties_path = os.path.join(base_directory, ".mvn/wrapper/maven-wrapper.properties")
    default_download_url = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.0/maven-wrapper-0.4.0.jar"
    url = default_download_url
    if os.path.exists(maven_wrapper_properties_path):
        with open(maven_wrapper_properties_path, "r") as f:
            for line in f:
                if line.startswith("wrapperUrl"):
                    url = line.split("=")[1].strip()
                    break
    maven_wrapper_jar_path = os.path.join(base_directory, ".mvn/wrapper/maven-wrapper.jar")
    if not os.path.exists(os.path.dirname(maven_wrapper_jar_path)):
        os.makedirs(os.path.dirname(maven_wrapper_jar_path))
    download_file_from_url(url, maven_wrapper_jar_path)
    print("Download complete")

if __name__ == "__main__":
    main()