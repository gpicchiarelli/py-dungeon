# py-dungeon
Modular python honeypot for **OpenBSD**
#### Installation procedure
```
tar -xvzf py-dungeon-{VERSION}.tar.gz
cd py-dungeon-{VERSION}
make all
doas make install
```
#### Uninstall procedure

```
doas make clean
```

#### Manual page

```
man dungeond
```

#### daemon handlers

```
doas rcctl enable dungeond
doas rcctl start dungeond
```
