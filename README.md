# AfterEffectsTrackingConverter

This Project is a helper for my video editing projects.

I really like After Effects for most 2D tracking applications and I think it surpasses Mocha Pro in this field.
But I don't like editing using Premiere. I edit the videos using Vegas Pro, and getting tracked Data from After Effects to Vegas Pro is something I didn't find much information about online.

This repository helps with that, using AE Scripting + Python for translating copied tracked data to a format that Vegas Pro understands.

First, you track your footage on AE and Smooth it using Smoother.

Then you can select the tracked data in AE and run the script from `TrackingCopier.jsx`.

You can then create a file called `input.txt`, paste the copied data from AE and run the python script.

It will generate a file called `output.txt`, which can be used on Vegas' Motion Tracking.