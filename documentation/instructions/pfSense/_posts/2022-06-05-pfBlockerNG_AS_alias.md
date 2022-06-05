---
title: pfblocker
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

- ipv4
  - alias name: `Netflix` 
    - will create an alias using `pfB_` plus this name
  - ipv4 lists:
    - format:   `Whois`
    - state:    `ON`
    - source:   `AS2906`
    - header/label: `netflix`
  - list action:    `Alias Native`
  - update frequency: once a day
  - states removal: `Enable`
