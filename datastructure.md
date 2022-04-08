{% include navigation.html %}

<h1>Data Structures Work</h1>
<h3><a href= "https://replit.com/@ReinhardtLotter/Menu?v=1">Replit Link</a></h3>
<h2>Hack One</h2>

![image](https://user-images.githubusercontent.com/89236857/162535907-4d69a2dc-06d6-49f0-a667-5a82714b17c3.png)

```
        <tr><th><label for="phone">Phone Number</label></th></tr>
<tr><td><input type="tel" placeholder="(858)999-9999" pattern="[0-9]{10}" id="phone" name="phone" size="20" required></td></tr>
    
```

<h2>Hack two</h2>

![image](https://user-images.githubusercontent.com/89236857/162536240-9f5c37a4-f4eb-4f2c-bde5-bcdcb06c837e.png)

```
<a href="{{ url_for('crud.crud_login') }}" class="navbar-item">
    Logout
</a>
```
<h2>Hack Three</h2>

![image](https://user-images.githubusercontent.com/89236857/162536348-7d138ccd-e7ba-41c5-bb6e-37ece84c84e3.png)

```
@app_crud.route('/search/')
@login_required
def search():
    """loads form to search Users data"""
    return render_template("search.html")
```
<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@ReinhardtLotter/Menu?lite=true#src/main.py">
    
