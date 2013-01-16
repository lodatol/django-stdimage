Django Standarized Image Field
==============================

Django Field that implement those features:

 * Rename files to a standardized name (using object id)
 * Resize images for that field
 * Automatically creates a thumbnail (resizing it)
 * Allow image deletion

Installation
------------

    Install latest PIL - there is really no reason to use this package without it

    easy_install django-stdimage

    Put 'stdimage' in the INSTALLED_APPS

Usage
-----

Import it in your project, and use in your models.

Example::

    [...]
    from stdimage import StdImageField

    class MyClass(models.Model):
        image1 = StdImageField(upload_to='path/to/img') # works as ImageField
        image2 = StdImageField(upload_to='path/to/img', blank=True) # can be deleted throwgh admin
        image3 = StdImageField(upload_to='path/to/img', size=(640, 480)) # resizes image to maximum size to fit a 640x480 area
        image4 = StdImageField(upload_to='path/to/img', size=(640, 480, True)) # resizes image to 640x480 croping if necessary
        image5 = StdImageField(upload_to='path/to/img', thumbnail_size=(100, 75)) # creates a thumbnail resized to maximum size to fit a 100x75 area
        image6 = StdImageField(upload_to='path/to/img', thumbnail_size=(100, 100, True)) # creates a thumbnail resized to 100x100 croping if necessary

        image_all = StdImageField(upload_to='path/to/img', blank=True, size=(640, 480), thumbnail_size=(100, 100, True)) # all previous features in one declaration

For using generated thumbnail in templates use "myimagefield.thumbnail". Example::

    [...]
    <a href="{{ object.myimage.url }}"><img alt="" src="{{ object.myimage.thumbnail.url }}"/></a>
    [...]

About image names
-----------------

StdImageField stores images in filesystem modifying its name. Renamed name is set using field name, and object primary key. Also it changes old windows "jpg" extesions to standard "jpeg".

Using `image5` field previously defined (that creates a thumbnail), if an image called myimage.jpg is uploaded, then resulting images on filesystem would be (supose that this image belongs to a model with pk 14)::

    image5_14.jpeg
    image5_14.thumbnail.jpeg


Copyright and license
---------------------

Copyright (c) 2012-2013 Pivotal Energy Solutions.  All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.