from setuptools import setup


setup(
    name='grow-ext-google-forms',
    version='1.0.3',
    license='MIT',
    author='Grow SDK Authors',
    author_email='hello@grow.io',
    package_data={
        'google_forms': ['*.html'],
    },
    packages=[
        'google_forms',
    ],
)
