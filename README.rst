This is a fork of a fork of ``clean-image-crop-uploader`` by Alfredo Saglimbeni and Michael Jones.

Changes:

* removed non-working pypi metadata
* removed south migrations, added Django 1.9 migrations
* removed JavaScript auto discover from CicuUploaderInput to allow JavaScript files to be added to the bottom of the page
* small wording and template tweaks


clean-image-crop-uploader (CICU)
================================

``clean-image-crop-uploader`` is a django widget to upload an image via Ajax and crop it using `Jcrop
<https://github.com/tapmodo/Jcrop>`_. It provides a simple workflow: first one, using modal,
(by `twitter bootstrap <http://twitter.github.com/bootstrap/javascript.html#modals>`_) the image can be uploaded and cropped.
Second one, you can see the image cropping preview in the form and finally submit the result.

``clean-image-crop-uploader`` is perfect when you use an ImageField on your model where is necessary to have a specific portion of image. It's easy to configure and to use.
You can use different configurations , with fixed aspect ratio or minimal image size.

It works with jQuery = 1.8.3 and twitter bootstrap.

Installation
------------

#. Install django-image-cropping using pip. For example::

    pip install clean-image-crop-uploader

#. Add ``south`` and ``cicu`` to your INSTALLED_APPS.

#. run migrate commando to your django project::


    python manage.py migrate

Dependencies
------------
* jQuery = 1.8.3
* Twitter-Bootstrap

Configuration
-------------
#. Add into url.py ::

    (r'^ajax-upload/', include('startproject.cicu.urls'))

#. Create your model-form and set  CicuUploaderInput widget to your imageField  ::

    from cicu.widgets import CicuUploaderInput

    class yourCrop(forms.ModelForm):
        class Meta:
            model = yourModel
            cicuOptions = {
                'ratioWidth': '600',       #fix-width ratio, default 0
                'ratioHeight':'400',       #fix-height ratio , default 0
                'sizeWarning': 'False',    #if True the crop selection have to respect minimal ratio size defined above. Default 'False'
            }
            widgets = {
                'image': CicuUploaderInput(options=cicuOptions)
            }

#. Download `twitter bootstrap <http://twitter.github.com/bootstrap/>`_  to your static file folder.

#. Add in your form template links to jquery, bootstrap, form.media::

    <head>
    ....
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <link href="{{ STATIC_URL }}css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <script src="{{ STATIC_URL }}js/bootstrap.js"></script>
        {{ form.media }}

    ....
    </head>
