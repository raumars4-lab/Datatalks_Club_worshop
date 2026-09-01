# Docker generations structure
I not going to describe what is the functional of dockerfile, I am going to build a generic code to build a dockerfile 
### Python version
-> FROM. version from python that is going to use this images
### Virual envirorment configurations and directories
-> COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 
              This sencence is a official uv image to generate dockerfile
-> WORKDIR. It is going to be the directory from the files, it is convencional, we can put /APP, /CODE...)
-> ENV PATH="/app/.venv/bin:$PATH" 
              It is using to add virtual envirorment to PATH to isntall packages
### Copy dependences necesary to docker
-> COPY "pyproject.toml" "uv.lock" ".python-version" ./ 
              Dockerfile copy the dependences taht it create during the virtual envirorment construcctions
              pyproject.toml -> It can introduce all the librearies taht we need to work and when docker are running, it is going to install all of them.
              uv.lock -> It is a file that show to docker where it can find the dependences (it is going to link pypoject.toml)      
-> RUN uv sync --locked 
              This sentences execute uv.lock that it has all the dependences and install inside the dockerfile
### Copy functions that is going to work inside script.
-> COPY main/ ./main/
              That is an example, in this case, docker is going to copy all the files inside main folder. This copies is going to save inside a folder with MAIN name. In this case, we have 2 folder inside main. The first folder has 10 functions and the second has 5 functions differents. docker is going to create an images with two folders with the same numbers of functions.
### Copy aplication code
-> COPY pipeline_wokshop.py .
              This is an example of script copy. That is the main script tha tis going to run whrn the docker is execute
-> ENTRYPOINT ["python", "pipeline_wokshop.py"]
              This sentences is going to be the execute docker image
