# MitmFox Client

> A mitmproxy addon that sends data to a MitmFox server.

## What is MitmFox?

MitmFox ([Man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)-Fox) is a system for developers
and testers to analyze [HTTP](https://en.wikipedia.org/wiki/HTTP) requests and server responses from client machines.
Developers can identify problems that occurred during testing on one or multiple clients without requiring physical
access to the client machines.

You can find the server software [here](https://github.com/gregor-gottschewski/mitmfox-server).

## How does it work?

The client machine runs a Python script (MitmFox Client) that intercepts network data via a
[proxy](https://en.wikipedia.org/wiki/Proxy_server) server and sends requests and responses to a MitmFox Server.

### How does a Proxy work?

Let's illustrate the basics of a "man-in-the-middle" with a short story:

You want to write a letter to Alice with the top-secret recipe of your grandma's brownies.
There is just one catch: you and Alice do not know each other's physical addresses. However, you both share a mutual
friend, Mallory, who is aware of both addresses.

So Mallory provides you with Alice's address: _Long Street 276, 1234 City, Wonderland_ and you send your letter to
that address.

What happens next? **Mallory** unfolds the letter. Mallory? Why not Alice? What happened?

The address _Long Street 276, 1234 City, Wonderland_ was not Alice's but Mallory's. So Mallory opens it, reads it and
may even modify it. Now, because he knows Alice's real address, he sends the letter away to Alice's real address.
Since neither Alice nor you know each other's addresses, you have to trust Mallory. Alice and you will never find out
about Mallory's actions.

A proxy does a very similar thing too (maybe a little bit more complicated).
To summarise that in one sentence, your computer believes it is communicating with the server, and the server believes
it is communicating with the client. In reality, both are communicating with a proxy.

## MitmFox Client

The [MitmFox Client script](mitmfox_main.py) is a mitmproxy addon that sends intercepted data to a
[MitmFox Server](https://github.com/gregor-gottschewski/mitmfox-server). It sends the header and body of requests
and responses to the server.

## Installation and First Steps

1. install mitmproxy and requests: `pip install mitmproxy requests`
2. [install the mitmproxy certificates](https://docs.mitmproxy.org/stable/concepts-certificates/) on your system or
browser
3. change your browser settings to use mitmproxy as a proxy (URL: http://localhost, Port: 8080)
4. `git clone https://github.com/gregor-gottschewski/mitmfox-client`
5. `cd mitmfox-client`
6. `python3 mitmfox-client.py http://<mitmfox-server>:port`

You should see an output like that:

```
[17:40:11.000] Loading script /path/to/mitmfox_main.py
[17:40:11.003] HTTP(S) proxy listening at *:8080.
```

## Disclaimer and Licence

**This application was developed for testing, development, and educational purposes ONLY.**

> MIT License
>
> Copyright (c) 2023 Gregor Gottschewski
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
