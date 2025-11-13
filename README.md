Instructions

Launch two seperate terminals. In one terminal run the following command 

```docker run --rm -p 5000:5000 vnach291/hurr-pred:latest```

In another terminal, make sure you have the following file structure within a directory

parent/data/damage
parent/data/no_damage
parent/grader.py

Given the above file structure you can now run the following command below in an alternate terminal

``` docker run -it --rm -v $(pwd)/data:/data -v $(pwd)/grader.py:/grader.py -v $(pwd)/project3-results:/results --entrypoint=python  jstubbs/coe379l /grader.py```

The HTTP server should work properly after this!