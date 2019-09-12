# -*- coding: utf-8 -*-
import re
import preprocessor as p

emoji_pattern = re.compile("(u[0-9][0-9][a-f][0-9])|(u[0-9][a-f][0-9][0-9])|(u[a-f][0-9][0-9][0-9])|(u[0-9][0-9][a-f][a-f])|(u[0-9][a-f][a-f][0-9])|(u[a-f][a-f][0-9][0-9])|(u[0-9][a-f][a-f][a-f])|(u[0-9][0-9][0-9][0-9])|(u[0-9][0-9][0-9][a-f])|(u[a-f][a-f][a-f][0-9])|(u[a-f][0-9][a-f][0-9])|(u[0-9][a-f][0-9][a-f])|(u[a-f][0-9][0-9][a-f])|(u[a-f][a-f][a-f][a-f])|(u[a-f][0-9][a-f][a-f])|(u[a-f][a-f][0-9][a-f])")
newtxt = emoji_pattern.sub(r'',tweetstxt)
newtxt = newtxt.replace(r"\n","")
p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.NUMBER,p.OPT.RESERVED)
newtxt = p.clean(newtxt)
rtpattern = re.compile("RT\s:\s*")
newtxt = rtpattern.sub(r'',newtxt)

