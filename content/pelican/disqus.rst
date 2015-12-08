Enabling Disqus on your Pelican blog
####################################

:date: 2015-12-08 10:38
:tags: Pelican, Disqus
:category: Pelican
:slug: pelican-disqus
:authors: Élysson MR
:summary: Connecting Disqus and Pelican

Disqus enables people register using their cendential of Twitter_, Facebook_, Google_ or Disqus_ to comment blog posts.
If you are using Pelican_ to generate a blog, using Disqus is really simple, just have to add some cinfiguration. All Pelican's standard themes are ready to use with Disqus, maybe all `downloadable themes`_ are ready to be used with Disqus.

The First step is create a Disqus account, just access `their site <https://disqus.com/admin/signup/>`_ and create a account. Now we need to register disqus to be used in a blog. Open the `Disqus Engage <https://publishers.disqus.com/engage/>`_ then click in "Starting using Engage" you should be redirected to a form, fill this form using your blog info and click "Finish registration". Remmember the value you put in Disqus URL, we are going to use this value to configure our Pelican Blog. We are done in Disqus for now.

After you create your pelican blog, open your "pelicanconf.py" and add a new configuration line:

.. code:: python

    DISQUS_SITENAME = 'DISQUS_URL_VALUE'



.. _Twitter: https://twitter.com_
.. _Facebook: https://facebook.com_
.. _Google: https://google.com_
.. _Disqus: https://disqus.com_
.. _Pelican: http://blog.getpelican.com/
.. _downloadable themes: http://www.pelicanthemes.com/

