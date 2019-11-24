
This Repo contains a yamlMerger.py which takes absolute file-path of a yaml file, lets call it childObject , then it start travesing to its parent directories, looking for yaml file with same name. once it don't find a file in parent directory it stop travesing furter.

once it have list of parent directories. lets call the file in parent directories parentObject. then it start merging the objects of child and parent. 

while merging the elements, the priority is given to the child elements, incase the same elements at same path present in child and parent object.

to execute the script simply call the script with passing file name as argument.

executing script::
------------------

[root@localhost yamlmerger]# python yamlMerger.py -f /root/nokia/dir1/dir2/dir3/dir4/input.yaml

Before Merging Yaml File::

count: 2

size: 8

todo:

  dishes:
  
    priority: low
    
  vacuum:
  
    priority: high
    
wishlist:

- worldpeace

Files for Mergning ['/root/nokia/dir1/dir2/dir3/input.yaml']

After updating the object::

color: blue

count: 2

size: 8

todo:

  dishes:
  
    priority: low
    
  laundry:
  
    priority: low
    
  vacuum:
  
    priority: high
    
wishlist:

- worldpeace

- car

- pony


This repo also got testYamlMerger.py for executing the unit tests.

executing unittests:
--------------------

[root@localhost yamlmerger]# python testYamlMerger.py

UnitTest for Dictnary Merge is success

UnitTest for List Merge is success

UnitTest for String,Int and Float Merge is success

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK


This repo also got .travis.yml for Travis CI for integration with Travis.
