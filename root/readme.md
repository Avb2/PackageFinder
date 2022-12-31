<body style="text-align:center; background-color: white;">
<h1 style="color: teal;"><u>Package Finder using Pypi</u></h1>
<div style="border-top: 1px black solid; color: black;">
<b>
<p>Using BeautifulSoup4, pyperclip, requests, and tkinter, I created this program to reduce the time it takes to install packages into a virtual environment. This program scrapes <a <a href="https://www.pypi.org/"> pypi.org</a> using BeautifulSoup4 to quickly find the pip install command for any package listed on Pypi. There are 2 versions available in this repository; one has auto-copy enabled, the other offers the user an option to copy to their clipboard manually.</p> 
<br>
<p>Thank you for using Package Finder made by AVB2!</p>
</b>
<br>
<h3 style="text-indent: 18px; text-align: left;">Instructions:</h3>
<ul style="text-align: left;">
<li>Open the program and run 'root/main.py' for the manual-copy version and 'root/auto-copy.py' for the auto-copy version</li>
<li>Type the name of the package that you are searching for into the search bar</li>
<li>Press the enter button</li>
<br>
<h4 style="text-indent:-14px;">If you are on the manual-copy version:</h4>
<li>If the name of your package was found, the 'pip install x' command will be displayed to you in the tkinter widget</li>
<li>You can then copy the output or clear for the next search by clicking the copy or clear buttons</li>
<li><b>it is highly recommended that you clear between each search</b></li>
<br>
<h4 style="text-indent:-14px">If you are on the auto-copy version:</h4>
<li>You are done! If the name of your package was found, the 'pip install x' command will be copied to your clipboard and ready to be pasted</li>
<li>You could also search for another package, but <b> it is highly recommended that you clear between each search</b></li>

</ul>

</div>

</body>