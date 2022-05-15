# # import keyword can be used to import a module/ file
# # it also can be used to import a package.(a directory of modules). It's a folder of organized python files
# # we declare a directory as a package by creating a __init__ py files inside that folder
# # this __init__ py files are not meant to be execured directly as script files by us
# # rather, Python runs them automatically the first time a program imports that directory that package.

# #                                Modules
# #                                   |
# #                   project folder (a standalone python application)
# #                           /                         \
# #                       main.py                  feature directory
# #                                               /           |        \
# #                              subfeature directory    __init__.py  calculator.py
# #                                  /    \
# #                       __init__.py    copyright.py


# # main.py is the launching point of our program

# # can import module(copywrigh.py) within the package or package itself (feature)
# # But, whenever we import any module within the feature directopry, such as copywrigh.py,
# # Python will auto liik for __init__.py file in the same folder
# # if it can find this file, it will auto execute the code within it.

# # only this line, we can run the __init__.py file with the same folder -- print : I'm the __init__.py file inside the 'feature' folder
# # import feature

# # if we want to achieve the attribute from the file. stil invoke __init__.py file first.
# # import feature.copyright

# # print(feature.copyright.date_of_copyright)

# # inovke both _init_.py files.
# import imp
# import feature.subfeature

# import feature.subfeature.calculator

# print(feature.subfeature.calculator.subtract(10, 3))

# from feature import subfeature
# from feature.subfeature import calculator

# using __init__.py to reduce the mult-level directory import complexity
import feature.subfeature
print( feature.subfeature.subtract(10, 2))
