**

**********************

498. Diagonal Traverse

**********************

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Â 

Example 1:

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAFOAU4DASIAAhEBAxEB/8QAHQABAQABBQEBAAAAAAAAAAAAAAgBAgMGBwkFBP/EAE0QAAEDAwICBgYHBgQCCAcBAAECAwQABREGBxIhCAkTIjFBFBlRdpa0MjY4VFZx0TdSYYGh0hUWI2IYkSgzQ2ZocqbkFzRERpeksdX/xAAaAQEAAgMBAAAAAAAAAAAAAAAAAQMCBAYF/8QANBEAAgEDAgUCBgECBgMAAAAAAAECAwQRMUEFElFhwSFxEzJCYoHwBqGxFBZSkaLRFSIz/9oADAMBAAIRAxEAPwD1TpSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUArim5Wrr1oXQ911Vp7Q911hcbe2hUeyWtTaZMtSlpThBcISMBRUT+6k4BPKt+PrTSF91DetB2fV8BzUNojNO3CFFktrlwUPhQacW2c8JPCSOIeQyMEZ+ZtnpG4be6MtWh5ur77qtdsY7FV3vbyHZknvE5cUlKQcZwOWcAAk+NSlkGdfbs6N2v0zG1ZrmZIt8KTNh25IbiuSHPSJLqW20cDSVKOFK54HIAmuaJcQv6KgcV+NduYWgpWhKgVJWAoZHECCD+YIBH8RXALtd93rTu3YrTatK2SRt7Itcx67XZ65LTNYmpW0GW0Mhsgggr5cWFDiJUgoSlxhPQHZtK2o76ZDYcT4Gt2oApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUrFAZrr7cjcfU2idS6Kstl2wvmpoep7qu33C4wHGEtWhoMOOB50OLSSMoHljAUASsoQv7mto2or7o3UFn0DqiJZtROw34kG4uMCUmBLU3lta2uIcRTxJVwk+YOCOR3NPM3hFjg2vUl0bulzjxmmps5qL6MiS8EgLdS0FKDYUQTwgkDOKlA1NWGypu03UdstUNi5XNDLc2Y0wlL0lLQUGg4sDKwkLUBknAJAr7bTfAkZHe9taIsVEVHCmt+oArafjtyE8KxkVu0oDrS222FsvB1nq7V25l1m2SZcHr/IkX+U0I9lj9khKmWlJQngYT2ZISc4zgc8k87s94teoLZFvVkuUW4QJzKJEaVFdS60+0oZStC0khSSCCCDg1m8Wi2agtUyx3m3x50C4MORZUaQ2HGnmlpKVoWk8lJIJBB8Qa6+1prPUO22odD6Z0ztVd79ab9cTa5Uq1mO1GscZEdxaXFpWtOEjs0gAAJ4QoA8fAhYHaFK2mJDchPEg5FbtAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClYPhXnV0Teidt3v9t5etda61Tr9q5NavvlsSm26qlxWAwxLWGgGgopTwpIThOBhI5eJIHorkUyKlX1buxH4w3U+Npn609W7sR+MN1PjaZ+tAVVkUyKlX1buxH4w3U+Npn609W7sT+L91PjaZ+tAVVkUyKlX1buxH4w3U+Npn609W7sR+MN1PjaZ+tAVVkDzrGfZUq+re2Iz9b91PjaZ+tfB1l0B9jtI2Zy8My96r2Wxj0a16vlPPnl5IKwSPyz+VQ2kssmMXOSjHVljk5/OuA3neHTFi3bsezcu235V4v9rl3ViUza33ILbbC20qS5ICeBJPae3CcJCikrbCvMzU+3mjF3tNm0tatw7a8HQx6PddZ3J+SpwnCRwpW3wE5HdwfzrsfoTdEDaXfbZyTrzUt31xAmDUl1gNt2vVEuM12DL/C3lHEe8EBKSfPhBPPJNNG5p1m1HY9K/wCEXHDacJ3GE5aLOX7+np/UvfSW2+jdBTr/AD9EWCNbHNVXVy9XZTWSZMxaEpU4ck4yEDkMAc8AZNcybbQjvADJ8alcdW5sMkYTq7dMD+Gtpn61n1buxH4w3U+Npn61e2eYVVkUyKlX1buxH4w3U+Npn609W7sT+L91PjaZ+tAVVkUyKlX1buxH4w3U+Npn609W7sR+MN1PjaZ+tAVVkVtvsokNlCjyNSz6t3Yj8YbqfG0z9ax6t3Yf8YbqfG0z9aA7wstm15Zdfahu921jDuGlrhGht2ezt23snbc8jtO3Up/jPahzKDzSMYwMAc+ZRJkebGamRX232XkhbbjawpK0nwII5EfxqTZHV6bDNTGorF/3Knr4gXWJGs5pZUjzC+FQOCOWAQeddN9DrombH7+7UTtwXIWq9Ht/5iudujWrT2qp0eK0xHcDbZKStXE4UgcahgKPPhHhXlWvF6F9dVLa3Tkqfo5LHLn/AE5z6tb409DOUHFJvf8Acno/kUyKlX1buxH4w3U+Npn609W7sR+MN1PjaZ+teqYFVZFMipV9W7sR+MN1PjaZ+tPVu7E/i/dT42mfrQFVZFMipV9W7sR+MN1PjaZ+tPVu7EfjDdT42mfrQFVZA86xnHhUq+re2Iz9b91PjaZ+tfB1l0B9jtI2Zy8My96r2Wxj0W16vlPPnl5IKwSPyz+VQ2kssmMXOSjHVljk5GPOsDA8RXkfqfbzRi72mzaWtW4dteDoY9Huus7i/JU4ThI4Urb4Ccju4P513b0DNwd1rW23o+HZrfP0Qi/akRc7tNujy57L7MttqMhKVJUXAG0Ed5XMZJUngAcrt68LmUo09j0r/hFfhtOE7jCctFnL/p6f1PQelbMaQmQ0HE+Yreq08wUpSgFKUoBSlKAUpSgMHwqVere/YRf/AH/1J84qqqPhUq9W9+wi/wDv/qT5xVAVXSlKAUpSgFKVjNAY/lXVW5m5l2ReW9sNsGGp+sZ6OJ11Xej2iOfGQ+eYzg91HiSRyOQFNzNzbw3eG9sNsWWp2sZ6OJ11XeYtEc+Mh88xnB7qPEkjkcgK5DtntlZ9t7OuLFecn3Ocv0i63SQeKRNkHmVrJycZJwnOAD5kkmmUnN8sfy/C7m/SpRtoqtWWW/lj17vt0W/sdXNdFu2WzW+hdSMyXrk7a5UibqCdKVxPTpPCFsunJ5YdT4c+WPE5J4L1Wn2YH/e++fMVX+c8qkHqtMf8ML/vffPmKmnRhSzyrUqub2tecvxpZ5Vhf7tlgUpSrTVFKUoBSlYJoDFfKuNxd7UW+3gKkKHM+TY9p/SlwuL3aC328BUhY5nybHtP6V+m3W5qA0QDxOK5rWrxUfaa4+9va/G68uG8Nk4wi8VKi26wg95Pd/T7l8Yqmueeuy8sxbrc3AbwO84rmtZ8VH2mpO6rT7MD/vffPmKr7GKkHqs/swv+998+YrpLKyt+HW8ba2iowSwv3dvVvcqlJzeZalgUpStwxFKUoBSlYoDH8q6q3M3MuyLy3thtgw1P1jPRxOuq70e0Rz4yHzzGcHuo8SSORyApuZubeG7w3thtiy1O1jPRxOuq7zFojnxkPnmM4PdR4kkcjkBXIds9srPtvZ1xYjzk+5zl+kXW6SDxSJsg8ytZOTjJOE5wAfMkk0yk5vlj+X4Xc36VKNtFVqyy38sevd9ui39jq5rot2y2620LqNqS9cnbXLkTdQTpS+J6dJ4Qtl0gnlh1Phz5Y8TknpLq+2EP6Z1AhwZH+db/APOrq8s1CXV6/VvUHvrf/nV1fbUoUubkWMr/AKKbu9rXnJ8aWeX0X5bfkqO1W6Dsxb9Zau1duXdZlkmT3r/IkX+U0I9lj9khKmWVBCeBhPZkhJzjOBzyTzyz3i16gtkW9WS5RbhAnMokRpUV1LrT7ShlK0LSSFJIIIIODWLraLZqC0S7HerfHnQLhHXFlRpDYcaeaWkpWhaTyUkgkEHxBrgGtNZ6h221DofTOmdqrvfrTfribXKlWsx2o1jjIjuLS4tK1pwkdmkAABPCFAHj4ELg1jtClbTEhuQniQcit2gFKUoBSlKAUpSgMHwqVere/YRf/f8A1J84qqqPhUq9W9+wi/8Av/qT5xVAVXSlKAV+O43GDZ4Em63OYzEhw2lPyH3lhDbTaRlSlKPIAAEk1+yvPfpZbO9NrpYbw3rZ6x3ZrReyVtVHD1zWnsU3IlpK15QFdrLIUogJHAzlPM8QzQHYHRo6xexdJnpCX3ZXS+264VotkKbPhahVee1M5ph5ttKvRuwT2YWHOIf6qsADxzy7x3M3Nu7d4b2w2wZan6xno4nXVd6PaI58ZD55jOD3UeJJHI5AV5O9XJoPdDSPSE1FM0JCZdfct9y03BnSxwISRJa7SXwc8obSyfaONSQOLmK9hNs9srPtvZ3IsR5yfc5y/SLrdJB4pE2QeZWsnJxknCc4APmSSaZSc3yw/L8LuehTpRtYqtWWW/lj17vt0W5p2z2ytG29pcjRXnJ9znL9Iul0kHikTZB5laycnGScJzgA+ZJJ5qPHFMHyrPjyFWRiorCNKpVlVk5zeWzNSB1Wf2YH/fC+fMVX9SB1Wf2YH/fC+fMVkYFf0pSgFSJ0rOsl2a6MGpHNBG0XLWGr2G0uSbdbnUMsQ+IApS++rPCspIISlCzgjOMiq7qO9AdXLpDR/SindJq/6/k6qmTJk25JtVztLZQzLfOUOIdC/wDsgSEgoJ8DnIzQHWmy/XJbR6/1RE01uZt3ctApnvJYZuSbmi5Q2lqOAXldk0ttPh3ghQHngZNXrMuvbluPaVoecfSFBxJylKSMhWR4jHhUXdZHttsRqRekNx94XWosDSb7xmtwUD/Er8paU+j2tkjCiVrBUTnuIBPd4uNNcbTxJLG3mnn7hYmbNNftkZ163tZ4YZLYIYGQOTYIR4D6PgK5K+u7jjdV8P4bJxgnipUW3WEHvJ7vSK76Xxiqa5p67Ly+xyS3W5uA3gd5xXNaz4qPtNftApjFB410NlZUOHUI21tFRgl++7e73KZSc3l6mqpA6rP7MD/vhfPmKr+pA6rP7MD/AL4Xz5itwgr+lKUAqTOlv1jG0fRUvadESbNcdW6vUwmS5a4DqGWoqFc0du+rPAVDmEpQs45kAEZrOpyuHQ46O2md7bj0tb5FuS9RQxIus12bK9JhoUGcF8MqQpQU2hPc4CMYGAaA6h6NXWw7S7660gbd6y0ZO0Beru6GLc49PROgvvE4S0XwhtSFqPJOW+EnlxA4zSm5m5t3bvKNsNsGWp+sZ6OJ11Xej2iOfGQ+eYzg91HiSRyOQFece+tu0p08ulTpnWmw1nmSLNaorEZd5RBchuXeU28Vh3C0pcQwyCkKeWAfFIGcV6ebY7ZWfbSyKiRnXJ10mr9Iut0kd6RNkH6S1KOTjJPCnPIHzJJNMpOb5Ifl+F3PQp0o2sFXrLLfyx8vt23G2e2Vo23tLkaK85Puc5fpF0ukg8UibIPMrWTk4yThOcAHzJJPNR44pg+VZ8eQqyMVFYRpVasqsnOby2Y9tQl1ev1b1B763/51dXb7ahLq9fq3qD31v/zq62KH1exWXaj6KfyrRIYTIbLavA1rR9FP5Vqqkk4JZbLr2ya+1DdrvrGHcNLXCNDbs9nbtnZPW55HadupT/Ge1DnEg80jGMDAHPmUOZHnRmpkR9t5l5AW242sKStJ8CCORH8aTIkafHdhy2EPMvIU242tOUrSRggjzBBxXV9lc2e6N0LQ+ztrdi6Yt96luWjTVuCXViRICVPLR2mFYUe8crUMkgDmQKag7ZpWlKkqGUnNaqAUpSgFKUoDB8KlXq3v2EX/AN/9SfOKqqj4VKvVvfsIv/v/AKk+cVQFV0pWKAx/Kuqtz9zbs3dk7YbYsNz9Yz2yp11XOPaGCOch8+AOD3UeJJHI5AU3M3NvDd4b2w2xZanaxno4nXVd5i0Rz4yHzzGcHuo8SSORyAr7+222No24sb0SI47cLrPUX7ndJJzInSDnK1qPMDJOE5wAfMkk0yk5vlj+X4Xc9ClShbRVasst/LHr3fbp1PLnq3NYXnVPTy1JHuUjMW0acvMKHHRybabRMjpyB+8rGVHxJ/hgV6+DxxXmb0Cuh70jNlulzqnc/czbn/B9MXG3XaPGnf4vAkdo49LacaHZsvrcGUoUclIAxzwa9NKsjFRWI6GnVqzrTc5vLYpSlZFYqQOqz+zA/wC+F8+Yqv6kDqs/swP++F8+YoCv6UrBNAYrqTpDdITRewOi5WqdUz1IKSGI0dhIXJlyVD/TjsN/9o6vyHgkZUrAHPsW5XF4L9Atye0kKTzxjCB7T5flXkV0kOjN1l2++8Du4qtsJ1uYs8xw6ZZhautTBtjKV5bcbUJgUHlYSpbnJRV7AEpTyd1e1eOV5cO4fJxhF4qVFt1hB/6nu/pXcvjFU1zS12Xl9io9j+i5uPvzuZbulF0uIyogt6/SdGaBKipm0oJCkPys/TeJCVFJGSoArxgNpukD+NeK/wDw09ch+It1f/ywx/8A6NesnR9tGvtP7HaFsu6Ts13WEKwQ2L2ubNEyQqalpIdLj4WsOq4s5WFKz45NdHa2lGxoxt7eKjCKwkv3ffq/VlMpOby9TsWlKVskCpA6rP7MD/vhfPmKr+pA6rP7MD/vhfPmKAr+lKxQGP5VPO5e+ejdzmZeyG1V0hajv+pTMsctXaLRGgtpStEorc5cS0JS4OFBJBBzzwFcx3M3NvDd4b2w2xZanaxno4nXVd5i0Rz4yHzzGcHuo8SSORyAqLukj1fnSOtm4Fh3v6L+6D0zUdna43Ik6WiLITMUSXXmFLHYrS6VHjbdI9hUsHAplJzfLH8vwu/9j0KNKFtFVq6y38sfL7dOp1d1hGzz/Q2VtTujspuBebHemS7altx5JabKmkpc7RtpPJLavoKbOUkBAOeZPp9sbrmfubs5orcK6wzEm6jsUK5SWCnh4HXWUqUMeXMnlXm/ZugR01+lZuHZdV9OHWrUGx2TDaoaZUNctxniBU0w1AHo7XHgBTmeLw5KIGPU2z2q3WG0wrFaIqI0G3x24sZlH0W2kJCUpH8AABVkYqCxHQ06tWdaTnN5bP3UpSsis0nzqEur1+reoPfW/wDzq6u0+dQl1ev1b1B763/51dXUNZexBdqPop/KtVaUfRT+VaqpJFcFuG4mlV7nsbSSIN0VfzZ1X5h9VqeVDDAdDSsSuHs0uBRT3cj6Q8+VbW8l63bsOmYcvZvSllv93VdoLUqPdbguI23BU+gSHEqShWSGyr/yjKgFlIbVyxDn+JNJCsIWB3glRIB8wDgZ/PFSgfqhNFtvmvizX6a22G+ybCM5xW5UAUpSgFKUoDB8KlXq3v2EX/3/ANSfOKqqj4VKnVvfsIv/AL/6k+cVQFVfyrqrczc27t3lG2G2DLU/WM9HE66rvR7RHPjIfPMZwe6jxJI5HICm5m5t4bvDe2G2LLU7WM9HE66rvMWiOfGQ+eYzg91HiSRyOQFch2z2ys+29nXFivOT7nOX6RdbpIPFImyDzK1k5OMk4TnAB8ySTTKTm+WP5fhdzfpUoW0VWrLLfyx69326Lf2MbZ7ZWjbe0uRorzk+5zl+kXS6SDxSJsg8ytZOTjJOE5wAfMkk81HjimD5Vnx5CrIxUVhGnUqyqyc5vLZmlKVkYClKUAqQOqz+y+/74Xz5iq/qP+qzP/Rff98L58xQFfV8q43F3tRb7eAqQocz5Nj2n9KXC4vdoLfbwFSFjmfJse0/pX6bdbmoDRAPE4rmtavFR9prj729r8bry4bw2TjCLxUqLbrCD3k939PuXxiqa5567LyzFutzcBvA7ziua1nxUfaa/aBTGKDxrpLKyocOoRtraKjBL99293uUyk5vmepqpSlbhApSlAKkDqs/swP++F8+Yqv6j/qs/svv++F8+YoCvv5V1VuZubd27yjbDbBlqfrGejiddV3o9ojnxkPnmM4PdR4kkcjkBTczc28N3hvbDbFlqdrGejiddV3mLRHPjIfPMZwe6jxJI5HICuQ7Z7ZWfbezrixXnJ9znL9Iut0kHikTZB5laycnGScJzgA+ZJJplJzfLH8vwu5v0qULaKrVllv5Y9e77dFv7GNs9srRtvaXI0V5yfc5y/SLpdJB4pE2QeZWsnJxknCc4APmSSeajxxTB8qz48hVkYqKwjTqVZVZOc3lszSlKyMBSlKA0nzqEur1+reoPfW//Orq7T51CXV6/VvUHvrf/nV1dQ+r2ILtR9FP5VxyNrfR1/1De9B2bWEB3UNmjtOXGDElNrlwEvhXZLW2c8BPCSOIezIwRn4W4m42pdE6j0VZbLthfNTQ9TXRcC43GA4wlq0NBhxwPOhxaSRlA8sYCgCVlCF8hZ09Y0XibqS1WqFHud0Qw1OmtMJS9JQzxBpLiwMrCAtQTknAJAqrBJ8vbbSU/QWjrVoifq6+aqctjPZKu16dQ7MkniJy4pKUg4zgcuQAGTjNcvYitR88AxmtTTfAkZHP21uVDYFKUoBSlKAUpSgNHlUE9DbcHUcDZ66bZ7cwfStXXjW2o5AfdQfRrZEM5aTKdOMHmCEp55I8DySq9vKvN3oo9DHaLpCbVy9T7i3HVzk60alvNij+gX12K36NHlrS3xIR3SvhIBVgZCR7KwnGUliLwbFtUpUm51FlrRbZ79v7l3bZ7ZWjbe0uRorzk+5zl+kXS6SDxSJsg8ytZOTjJOE5wAfMkk81HjipB9Vp0YfKZuB8VSKz6rToweUzcD4qkVMYqKwiqrVlVk5zeWyv6VIHqs+jB983A+KpFPVZ9GD75uB8VSKyMCv6VIHqs+jB983A+KpFPVZ9GD75uB8VSKAr+lSB6rTowffNwPiqRQ9Vp0YPvm4HxVIoCvajPqz3J8PoyehMxXEPTNVXt5pa0kDs/SinjyfEZSofmDRfVodGSJPYZhJ1xMeQtK1tPaplFrAOTx8JBwfYCDXDdhNhtsem7ti1uRuPGv1lZs13uOn7JZNP3l6FAt8CM9wNISyjulzhxxrwOLA5AAAcjeXtbjlaXDeGzcYReKlRbdYQe8nu/p99L4xVNc89dl5fYvG3W5uA3gd5xXNaz4qPtNftAqQfVa9GH73uB8VSKeq06MP3zX/xVIrorKyt+HUI21tFRglt++rerb1KZSc3mWpYFKkD1WfRg++bgfFUinqs+jB983A+KpFbhBX9KkD1WfRg++bgfFUinqs+jB983A+KpFAV/SpA9Vn0YPvm4HxVIp6rTowffNwPiqRQFe/yrzz6Be4OooHR2a2z25g+k6vu+p73ID7qD6NbIhlFJlOnGDzBCU88keB5JVncHoFdHaBqKLtztmxrS8avk8LrwkaplKiWyPkZeklJB8DyQCCcj2pCvi9EjokbO9KHZ1G4Gv2tRQpUG9XGzRYtlvL0OM3GjvcLf+mnlx48Vcs4FUSk5vlh+X4Xc9ClShbQ+PX9W/lj5fb+5eG2e2Vo23tLkaK85Puc5fpF0ukg8UibIPMrWTk4yThOcAHzJJPNR44qQfVadGH75r/4qkVn1WnRg8pm4HxVIq2MVFYWhpVasqsnOby2V/SpA9Vn0YPvm4HxVIp6rPowffNwPiqRWRgV/SpA9Vn0YPvm4HxVIp6rPowffNwPiqRQFf0qQPVadGD75uB8VSKeq06MA/8ArNwPiqRQFeeHKvPfoUwtR3fa3Xdr0Vf49mv0jU+pWLfcXo3pKIclUpzs3VNZHFwkhWCfZ4+B56vq0OjJEnsMwhriY8haVrae1TK7LhByePhIOD7AQa4/0EWbA+rWl+01paDYGbrre7qVChcXZNhl0MJxxEnmloKIGBxKXwhIISPO4fxilfXdW1t05KmsSkvl5vT/ANU92t/T0MpwcUnLf9yWbp9i7oscG2aiuaLnco8ZtqZObjCOmS8EgLdDQUoICiCeEEgZwK+1Fioio4U1qYbQlCVBIyRW7XpZMRSlKgClKUApSlAKUpQGD4VKvVvfsIv/AL/6k+cVVVHwqVere/YRf/f/AFJ84qgKrpSlAKUpQClKwTQGK+Vcbi72ot9vAVIUOZ8mx7T+lLhcXu0Fvt4CpCxzPk2Paf0r9NutzUBogHicVzWtXio+01x97e1+N15cN4bJxhF4qVFt1hB7ye7+n3L4xVNc89dl5Zi3W5uA3gd5xXNaz4qPtNSd1Wn2YH/e++fMVX2MVIPVZ/Zhf97758xXSWVlb8Ot421tFRglhfu7ere5TKTm+aWpYFKUrcIFKUoBSlYzQGP5V1VuZubd27yjbDbBlqfrGejiddV3o9ojnxkPnmM4PdR4kkcjkBTczc28N3hvbDbFlqdrGejiddV3mLRHPjIfPMZwe6jxJI5HICuQ7Z7ZWfbezrixXnJ9znL9Iut0kHikTZB5laycnGScJzgA+ZJJplJzfLH8vwu5v0qULaKrVllv5Y9e77dFv7GNs9srRtvaXI0V5yfc5y/SLpdJB4pE2QeZWsnJxknCc4APmSSZ26rP7ML/AL33z5iq+wfKpB6rP7MD4/74Xz5irIpRWFoadSrKrJzm8tlgUpSsjAUpSgFKVgmgMV8q43F3tRb7eAqQocz5Nj2n9KXC4vdoLfbwFSFjmfJse0/pX6bdbm4LRAPE4rmtZ8VH2muQvb2443Xlw3hsnGEXipUW3WEHvJ7v6fcvjFU1zz12Xli3W1uA3gd5xfNaz4qPtNQ91ev1b1B763/51dXaKhLq9Pq3qD31v/zq66nhdlQ4db/4e2iowitP3VvVtlE5Ob5mXaj6KfyrVWlH0U/lWqrgKUpQClKUApSlAKUpQGD4VKvVvfsIv/v/AKk+cVVVHwqVere/YRf/AH/1J84qgKrpSlAKUqPusd6VcjYPatvQmhpK17ia/CrbZ2o/efisrPA5JCRz4u8EN8ua1f7TQHwLr1n2kldKuB0bNGbdf5hhSr2xYXtTJvgZbRJUrhd4I4YX2iW1ZTntE8RB8BgmybjcXe1Fvt4CpChzPk2Paf0rx26OXQg1bs/0h9K6y3o1NHskSzXS1GGFf9fdL7JbQ4iEwCSVhpSwXXcY7igPBSkeyVutzUBogHicVzWtXio+01yN/eV+M13w3hs+WEf/AKVFt1hB7ye70iu/oXxiqa5p67Ly+xi3W5uA3gd5xXNaz4qPtNftApjFB410VlZUOHUI21tFRgl++7e73KZSc3l6mqpA6rP7MD/vhfPmKr+pA6rP7MD/AL4Xz5itwgr+lKUAqOumz1hsPoeaw09o9ra3/OMm925y4Or/AMd/w/0VIc4EJx6O7x8WFHORjHnmrFrxf6bO5G20/rLoEzdkiZonRJt0O7xnInpbbjbTJkLa7HBC+NbgSQRg554AOAOzPXl/+F7/ANbf+wq7tXbw3e8N2rRW18JuRrK/QWZrvErjj2Rh1CVF59WMEgK7qcZJwccwlUg2ne7oK7uWSLB2u6LugtM3G/XNFlttz1foqyQYnaLOO1bKS52hHkkgZPiDjhN17V7WWDaywf4ZbCZU6UQ7cbi6kdtLex9I+xI5hKRySPaSSaZSc3yx/L8LuehTpQtoKtWWW/lXXu+3RbmrbPbK0bb2lyNFecn3Ocv0i6XSQeKRNkHmVrJycZJwnOAD5kknmo8cUwfKs+PIVZGKisI0qlWVWTnN5bM1IHVZ/Zgf98L58xVf1IHVZ/Zgf98L58xWRgV/SlKAVOPSw6c2z3RKixoGrPTb3qe4tF6HYbaUduWskB15aiEstkggE5UcHhScHFHV4dW/c7a/WvWRat3X6Ql7jtaQ0rdrnKS3cGy82sQMsxGEMgKKzxpQpKAMkjw8aArbZbrj9qdwtZxNJbi7a3HQrFxkJjRbmm6JuMZC1HCS/hppTSSSBkBYGeeBki9p90U4pEO2FLrzqQrjBylKT5k//wAqFNb3LoYdO6LpjdLcHT+o9L2y1XYWCy3O/ORbPHv7jihhhCkOLeebSUEDBbwVLGcg4u+x2SFYYDMCC0lCGW0tJAHglIwAPYABgVyN/eXHGbiXDOHScYReKtTp9kHvJ7v6fcvjFU1zz12Xlm9brc3AbwO+4rmtZ8VH2mv2gUxigHOuisrKhw6hG2toqMEv33b3e5TKTm8vUe2oS6vX6t6g99b/APOrq7fbUJdXr9W9Qe+t/wDnV16ND6vYxLtR9FP5VqrSj6KfyrVVRIpSlAKUpQClKUApSlAYPhUq9W9+wi/+/wDqT5xVVUfCpV6t79hF/wDf/UnziqAqulKwTQH5LjNRbrfKuDiFLRFZW8pKfEhKSSB/yrx92v3Htevd29UdYj0o48uFpazPCNoa2rQhz0qQkqS0xFaUodqplIJz9DtVLUpQ4FY9dLtML/FaYzSXnHk8LgUApKUnkeIHkRjyridw6P2yN/tVrsuqdodE3yJZWewt7Fy0/EktQmyBlDCHGylpPdT3UADkPZXJ3V/V41Xnw3h7cYReKlRbdYQe8no3pFd8F6iqa55a7Ly+x4y7u9NrTe4/TJ0Zvk3/AJtXoLR0+BJi2qYywmY0lshUgoaS8WuNa8nJcyQEgkBIA9ntid5tL9ILa60bs6Lt91h2i9B1Udi6NNtyU9m4ps8aW1uJHNJxhR5Yrz43V6vvX916d1m1zono/acTs0zcrW5MZjm1R7eWEIQJPFALiVKHEFZT2R4vYa9MNLaT0voiyR9NaN03arDaYnF6Pb7XDbixmeIkngabASnJJJwPEmuitLOhw+3hbW8eWEVhL93erfUqlJzfM9T7NKUraMRUgdVn9mB/3wvnzFV/UgdVn9mB/wB8L58xQFf0pWKAx/KvPLcDYXojbldIGXqfbyCNc7lakucxmXGu0kv2OHKbyH33WXGwHltBtYDQK0ApPEkkJBrjczc28N3hvbDbFlqdrGejiddV3mLRHPjIfPMZwe6jxJI5HICor6THV79IyJr+w729GTc9+bqO0Nh1yLNmIiSETSSXX461DslJdJPGh0jlyKlg4FEm5vlj+X4Xc9CjShaxVaust/LHy+3Tqdb9aZ0a9udltmttb9pZC2L0zdXLQ+tCy23IaUwt0qSwDwNhC20hPABhKgCTyNeh/Q81TftbdF/bLVGqH3X7pP05EXJecJKnVBPCHCT4lQSFZ/jUD27oKdOrpZa5sd76bOt2rbp2xqIVEEqCuStriBUhhm3j0dClgYLqlcQGOSsYr1LsFitOmLHA01YobcS3WuM3DiMNjCWmW0hKEj8gBVsYqKwtDSq1Z1pOc3ls+jSlKyMBUgdVn9mB/wB8L58xVf1IHVZ/Zgf98L58xQFf0pWCaAxXjXsl0JXdc9LnVmpt6YcWHo9jXF2i22DcF9mdRzg+84llpBOXG0JBccIyDwFHPv8AD6/3C4vdoLfbwFSFjmfJse0/pUTdOnoR71bw6p0zvHsJuS/E1RpNr/QtMucqM2l0LK+3iOAcLbyicLC8BQSnKhjB5O6v63GrifDeHScYR9KlVbfbB7ye7+n3L4xVNc8tdl/32OpeuK2o0fpHajbPUlgiJtr9sujliiw4p7GK3EUwp3DbCcNt8KmUAFKRyIB8BVydDvVV91v0XdsdU6leceuc/TkRUl5zPE6pKeALOfEqCQrP8agH/gf6wPpaatsSemPrdq06ZsDhwFSbe4+pskcfYMQB2RcUBjtHSCB7fon1O0rpmzaM05bNJ6ehoiWyzRGoMNhPg2y2kJSP+QFdDZ2dDh9vC2t48sIr0/d29W92VSk5vmep9alKVtmJpPnUJdXr9W9Qe+t/+dXV2nzqEur1+reoPfW//Orq6hrL2ILtR9FP5VqrSj6KfyrVVJIpSlAKUpQClKUApSlAaTnFSr1b/wCwi/8Av/qT5xVVUc1JvV0zWYexV6S8rh7bcHUaE/n6YqtevcUrWm6laSjFY9Xp6vCJScnhFZV8q43F3tRb7eAqQocz5Nj2n9KXC5PdoIFvAVIWOZ8mx7T+lfpt1uagtEA8Tiua1nxUfaa5e9vq/HK8uG8Mk4wi8VKi26wg95Pd/T7l0Yqmueeuy8sxbrc3AbwO84rmtZ8VH2mv2gUxig8a6SysqHDqEba2iowS/fdvd7lMpOby9TVSlK3CBSlKAVIHVZ/Zgf8AfC+fMVX9R/1Wf2X3/fC+fMUBX38q6q3M3Nu7d5Rthtgy1P1jPRxOuq70e0Rz4yHzzGcHuo8SSORyApuZubeG7w3thtiy1O1jPRxOuq7zFojnxkPnmM4PdR4kkcjkBXIds9srPtvZ1xYrzk+5zl+kXW6SDxSJsg8ytZOTjJOE5wAfMkk0yk5vlj+X4Xc36VKFtFVqyy38sevd9ui39jG2e2Vo23tLkaK85Puc5fpF0ukg8UibIPMrWTk4yThOcAHzJJPNR44pg+VZ8eQqyMVFYRp1KsqsnOby2ZpSlZGApSlAKkDqs/svv++F8+Yqv6j/AKrM/wDRff8AfC+fMUBX1fKuNxd7UW+3gKkKHM+TY9p/SlwuL3aC328BUhY5nybHtP6V+m3W5qA0QDxOK5rWrxUfaa4+9va/G68uG8Nk4wi8VKi26wg95Pd/T7l8Yqmueeuy8sxbrc3AbwO84rmtZ8VH2mv2gUxig8a6SysqHDqEba2iowS/fdvd7lMpOby9TVSlK3CBSlKA0nzqEur1+reoPfW//Orq7T51CXV6/VvUHvrf/nV1dQ+r2ILtR9FP5VqrSj6KfyrVVJIpSlAKUpQClKUApSlAaT4cjUZdBaPNi7IzUraUlMnW2pJTGPFaf8Qcbz/JTahVH7x3rduxaZhy9m9K2W/XdV2gsymLrcFxG24Kn0CQ4lSUKyQ2Vf8AlGVALKQ2qIOiT0Q9tekHsq9cdx9Q66cFl1Te7RDhQ9TSI8NplmYvhKWEns0rPEeJSUp4jzIySTx384/jVx/LOFPhdCt8JSlFyljLxF5wllavHrn0wX21aNCpztZL/wBOJlIRh23qRx81OqVzUf4g86+7k5qQvVa9GEeMzX/xVIp6rXow/e9f/FUivT/jnBP8vcPhw9VXUUVjmaSf/FL/AHeX1bMKtT4s3PGMlgUqQPVZ9GD75uB8VSKeqz6MH3zcD4qkV7xWV/SpA9Vn0YPvm4HxVIp6rPowffNwPiqRQFf0qQPVZ9GD75uB8VSKeq06MH3zcD4qkUBXv8q88+gXuDqKB0dmts9uYPpOr7vqe9yA+6g+jWyIZRSZTpxg8wQlPPJHgeSVZ3B6BXR2gaii7c7Zsa0vGr5PC68JGqZSolsj5GXpJSQfA8kAgnI9qQr4vRI6JGzvSh2dRuBr9rUUKVBvVxs0WLZby9DjNxo73C3/AKaeXHjxVyzgVRKTm+WH5fhdz0KVKFtD49f1b+WPl9v7l4bZ7ZWjbe0uRorzk+5zl+kXS6SDxSJsg8ytZOTjJOE5wAfMkk81HjipB9Vp0Yfvmv8A4qkVn1WnRg8pm4HxVIq2MVFYWhpVasqsnOby2V/SpA9Vn0YPvm4HxVIp6rPowffNwPiqRWRgV/SpA9Vn0YPvm4HxVIp6rPowffNwPiqRQFf0qQPVadGD75uB8VSKHqtOjB983A+KpFAV7UZ9We5Ph9GT0JmK4h6Zqq9vNLWkgdn6UU8eT4jKVD8waL6tDoyRJ7DMJOuJjyFpWtp7VMotYByePhIOD7AQa4bsJsNtj03dsWtyNx41+srNmu9x0/ZLJp+8vQoFvgRnuBpCWUd0ucOONeBxYHIAADkby9rccrS4bw2bjCLxUqLbrCD3k939PvpfGKprnnrsvL7F4263NwG8DvOK5rWfFR9pr9oFSD6rXow/e9wPiqRT1WnRh++a/wDiqRXRWVlb8OoRtraKjBLb99W9W3qUyk5vMtSwKVIHqs+jB983A+KpFPVZ9GD75uB8VSK3CCv6VIHqs+jB983A+KpFPVZ9GD75uB8VSKAr7IArHgf41IPqtejDn/5vcD4qkV8HWXVu9GbSNmcvDVl3WvZbGPRbVqN558jHkgqBI/LP5VDaSyyYxc5KMdWW2f61CfV6/VzUHvrf/nV1Mup9kdpF3xNm0tobV9tdDoY9Huup5r8lThOEjhSW+AnI7uD+dUZ1cVqi2bSV8hQUqS0jWF5QEqWVYDcjsk8zknutjJJJJJOai0uYV5SUNkejxDhNxw2nCdxhOeizl+m/p6f1L7R9FP5VqrQ1/wBWn8q11keaKUpQClKUApSlAK41G1vo6/6hveg7NrCA7qGzR2nLjBiSm1y4CXwrslrbOeAnhJHEPZkYIz8PcjcfU2idS6Kstl2wvmpoep7qu33C4wHGEtWhoMOOB50OLSSMoHljAUASsoQvkDOnrGi8TdSWq1Qo9zuiGGp01phKXpKGeINJcWBlYQFqCck4BIFTgHytt9JT9BaNtWiJ+rb5qly2M9kq7Xp1DsySck5cUlKQcZwOXIADJxmuiercATsPfkjwGvtSD/8AcNVQ22EoAUOeKljq3v2EX/3/ANSfOKqGwVXSlKAUpSgFKVjNAY/lXVW5m5t3bvKNsNsGWp+sZ6OJ11Xej2iOfGQ+eYzg91HiSRyOQFNzNzbw3eG9sNsWWp2sZ6OJ11XeYtEc+Mh88xnB7qPEkjkcgK5DtntlZ9t7OuLFecn3Ocv0i63SQeKRNkHmVrJycZJwnOAD5kkmmUnN8sfy/C7m/SpQtoqtWWW/lj17vt0W/sY2z2ytG29pcjRXnJ9znL9Iul0kHikTZB5laycnGScJzgA+ZJJnbqs/swv+998+YqvsHyqQeqz+zA+P++F8+YqyKUVhaGnUqyqyc5vLZYFKUrIwFKUoBSlYJxQGK+Vcbi72ot9vAVIUOZ8mx7T+lLhcXu0Fvt4CpCxzPk2Paf0r9NutzUBogHicVzWtXio+01x97e1+N15cN4bJxhF4qVFt1hB7ye7+n3L4xVNc89dl5Zi3W5uA3gd5xXNaz4qPtNSd1Wn2YH/e++fMVX2MVIPVZ/Zhf97758xXSWVlb8Ot421tFRglhfu7ere5TKTm+aWpYFKUrcIFKUoBSlYoDH8q6q3M3MuyLy3thtgw1P1jPRxOuq70e0Rz4yHzzGcHuo8SSORyApuZubeG7w3thtiy1O1jPRxOuq7zFojnxkPnmM4PdR4kkcjkBXIds9srPtvZ1xYjzk+5zl+kXW6SDxSJsg8ytZOTjJOE5wAfMkk0yk5vlj+X4Xc36VKNtFVqyy38sevd9ui39jq5rot2y2620LqNmS9cnbZLkTdQTpSuJ6dJ4Qtl0gnlh1Phz5Y8Tknpfq9Pq3qD31v/AM6urtz/ABqEur1+reoPfW//ADq6vtaUaXNyrVf9FN3e1rzk+NLPL6L8tvyXaj6KfyrVWlH0U/lWqoNYUpSgFKUoBXG9aMahvukNQWnQWpYdn1E5Deiwrg7HEpECWpvLa1tBQ4iniSrhJ8wcEcjsau3L0Roa86Z09qvUDVvuOsLgbXZI6m1rVLkhsuFA4UkJwlJ7ysJ5gZyRX49IbZaM29uOoJ2htPxrYvVd2cvd3UyVH0mYtCEqcOScZCB3RgAkkDmalLIPr2Fm7oskG2ajuaLpcmIzbUyc3GEdMl4JAW6GgVBAUcnhBIGcCvsxYqIqOFNa22ko58I4vOtymQYPhUq9W9+wi/8Av/qT5xVVUfCpV6t79hF/9/8AUnziqgFV0pSgFeY2uOum/wAl621Bo/8A4bPTP8Cusu2ek/5x7PtuxeU3x8HoJ4c8OcZOM4yfGvTmuqrt0ZujDKem3y+dHva5151TkuZLlaTt61rUSVOOOLU1kknJKicnmTQEAevL/wDC9/62/wDYVZdl6SV53Z2+0YvbHT7cfWWuLHFvDsVcj0hjT7D7aVlx93gSFlIUOEcIKuR4eYSrzj/+E9l6anSmfnbQbTaX0xtpp6QuFbI9qske3s3JtpeFypBYQnibK+ZKsnh4W0jKjj1q2m2m03tLptFlsrQelPBK505aAHJLgGMnH0UDwSgckj+OSaZSc3yw/L8I9CnShawVasst/LHy+3Rbm5tntlaNt7S5GivOT7nOX6RdLpIPFImyDzK1k5OMk4TnAB8ySTzUeOKYPlWfHkKsjFRWEaVSrKrJzm8tmakDqs/swP8AvhfPmKr+pA6rP7MD/vhfPmKyMCv6UpQCpA6WnWT7R9FzUitAIsNw1lq5ppL0q3wZCI7EIKGUpffUFcKyCCEpQogEE4yM1/Xj/rq1Qeih1lc7ejpGaTmS9BX+5S7hab6YK5cdlx5v/SdASDlxk5SUAFY5KAPKgKD6P3W9bS7t6zt+htwNBT9AS7s+mNDmruaJ8DtVHCEOu9m0pviOADwFOTzIHOrnuVxcLot9vAXIWOZ8kD2moA3u0Lsx09dyNCbp6NhXO56SsCXoz1xi22RAl6mklxBbhRw6ht3sWilZdkqCUtgkJVnjUj0Bs1qRbITbXCntuBIcUDnnjyz5Dyrkr+7r8Zry4Zw6TjGLxVqL6fsi95Pd/Su5fGKprnnrsvL7G7brc3AbwO+4rmtZ8VH2mv2gUxig8a6GysqHDqEba2iowS/fdvd7lMpOby9TVUgdVn9mB/3wvnzFV/UgdVn9mB/3wvnzFbhBX9KUoBUe9LDrLtnujFqV3b+NZZ2tdXxkJXLt8GQiPHhFQylD8hQVwrIIPClCyB9LhyM1+sqCSpIyQOQ/jXjZ1dbFl1Z1het7ruKlqbqBlV8mQBOTxrE4SwFqSFZ/1EIK8eYGceHICtujB1qe0HSA1fC291PpadoLUVzX2VuTJmomQZTp8GhICGylw+QU2ATyCskA0VuZubdm7wjbDbBlqfrGejiddV3o9ojnxkPnmM4PdR4kkcjkBXn/ANaZo3am3706U3PenxLZNtUFbt9Tb8ImTpSXEKhN93H+pgOEqJ4gkJPIYIvbouW3Tz2zemtd2ttx6drO2Rb5cpz7vbPyn3mwslTnmkFRCR4AfxJJplJzfJHTd+F3PQpUo20FXrLLfyx69327bnKds9srRtvaXI0V5yfc5y/SLpdJB4pE2QeZWsnJxknCc4APmSSeajxxTB8qz48hVkYqKwjSq1ZVZOc3lsx7ahLq9fq3qD31v/zq6u321CXV6/VvUHvrf/nV1sUPq9isu1H0U/lWqtKPop/KtVUkilKUApSlAcK3Z19pnbDRkjXOrIVykwre8y2E262OzpHaPOJaRwNtpKhlS0ji5AZ5muT29aFsJWhSyFpChxpKVYPtBwQf4HnX7HE8aCnOM11pd7tu5ad3bHa7RpSySNvZFqmPXa7PXJaZrE1K2gyhDIbIIIK+XFhQ4iVIKEpclevoDs2lbUd9MhsOJ8DW7UAwfCpV6t79hF/9/wDUnziqqo+FSr1b37CL/wC/+pPnFUBVdKVigMfyqTen10lNH7WbUX3Rz10c/wARvEb0OWIrmHGGHRzbBByHXU8SUgYISVLJAAz27uZubeG7w3thtiy1O1jPRxOuq7zFojnxkPnmM4PdR4kkcjkBUddP7oX7x7g7e6I0hsZo9/V89m5y7tqa5yLlDivSZSm0oQ4tUl5BUO87wpTxcIJ55JJplJzfLD8vwu56FGnC1iq9dZb+WPl9unU726uzSItPRysuuZVqjQpesgbk2ww2EpjQASmIwn2gNji/ipxR5ZxVSDxxXEtp9Lu6J2w0lo52GmI7ZbJCgusJKSG3G2UpUnKSQcKB5gkH21y+rIxUViOhpVas603Oby2KUpWRgKkDqs/swP8AvhfPmKr+pA6rP7MD/vhfPmKAr+lKwTQGK8pbBs3rzp39KrUOvd+pc5vbDT98uFm03ZHZi2G55iuLQWo6EkHgAbUt51HeKhwAnBKPUW4XF7tBb7eAqQscz5Nj2n9KhHpi9DjpVai3ZsW+nRp3QAnafZCIFjfktw1W5wj/AFVRipPYOJdOVLS7gnwJUkJSnk7q/rcarz4bw6TjGPpUqrbrCD3k93pH3wXxiqa5567Ly+x1d1pelbr0drttFu5tFri66blWrtbLb7XCf7KLCQylKwphpOEpSodxxJBCwEA8hivRzZDXM3c3Z/Rm4dxhGJL1HY4dyfYKSns3HWkqUMHw5k8q80Y3QP6d/Sy3BsmoOmdq5i12SzEIWlUqC5JLHFlbcZi3jsEKXgAuKII5HvYxXqtYbHa9NWSBpyyxUxrfa4rUOKynwbabSEoSPyAFdFaWdHh9CFtbxxBLC/d29W+pTKTm+Z6n0qUpW0QKkDqs/swP++F8+Yqv6kDqs/swP++F8+YoCv6UrFAaRy8udeaHSS6Gm32sulhZ9ZbE7jP2rWl7muTbra7bL7BuPKbSSuQmW0vjjKPCorbQlS+SiOEkA23uZubdm7ujbDbBlqdrGejiddUOJi0Rz4yHzzGcHuo8SSORyAqIOkb0DuljpfdWz759F3cRy83e3tBfo0mWxElsS1JPbuI7fEd1t0lRUlxWe9g8QAIplJzfLH8vwu56FKlC1iq1dZb+WL37vt06+xMnWJ7C6n2ZOk7zubuV/mPWeqnpshyFFWtUOFEb4BkLdHavurWslTq+Hixjh5V7BdGXTEjRfR5230pLStL1s0vbY7gX9IKEdGQeQ51CO1XV/dJ/fneK0709PDVzElqzdkpuytyY7r8js1cSGVJiARmGeLmrsySrmCBnir05QhDSAhtISlICUpAwAB5VZGKguVaGnVqzrSc5vLZuUpSsis0nzqEur1+reoPfW/8Azq6u0+dQl1ev1b1B763/AOdXV1DWXsQXaj6KfyrVWlH0U/lWqqSRSlKAUpSgFbT8duQnhWMit2lAdaW22wtl4Os9Xau3Mus2yTLg9f5Ei/ymhHssfskJUy0pKE8DCezJCTnGcDnknndnvFr1BbIt6slyi3CBOZRIjSorqXWn2lDKVoWkkKSQQQQcGs3i0WzUFqmWO82+POgXBhyLKjSGw4080tJStC0nkpJBIIPiDXX2tNZ6h221DofTOmdqrvfrTfribXKlWsx2o1jjIjuLS4tK1pwkdmkAABPCFAHj4ELA7PPhUq9W9+wi/wDv/qT5xVVMzIbkI4kHIqWOre/YRf8A3/1J84qgKq/lXVW5m5t3bvKNsNsGWp+sZ6OJ11Xej2iOfGQ+eYzg91HiSRyOQFNzNzLw3eEbYbYstTtYz0cTrqhxMWiOfGQ+eYzg91HiSRyOQFch2z2ys+29nXFivOT7nOX6RdbpIPFImyDzK1k5OMk4TnAB8ySTTKTm+WP5fhdzfpUoW0VWrLLfyx8vt0W/sY2z2ytG29pcjRXnJ9znL9Iul0kHikTZB5laycnGScJzgA+ZJJ5qPHFMHyrPjyFWRiorCNOpVlVk5zeWzNKUrIwFKUoDHM4qQOq0+zA/z/8AvC+fMVXxyKjnqv5rEToxLS8rHa6yvaE/n6RWvXuKVrTdWtJRiser09Xhf3JScnhFjV8q43F3tRb7eAqQocz5Nj2n9KXC5O9oIFvAVIWOZ8mx7T+lfpt1uagtEA8Tiua1nxUfaa5e9vq/HK8uG8Mk4wi8VKi26wg95Pd/T7l0Yqmueeuy8sxbrc3AbwO84rmtZ8VH2mv2gUxig8a6SysqHDqEba2iowS/fdvd7lMpOby9TVSlK3CBSlKAVIHVZ/Zgf98L58xVf1H/AFWf2X3/AHwvnzFAV9/KuqtzNzbu3eUbYbYMtT9Yz0cTrqu9HtEc+Mh88xnB7qPEkjkcgKbmbmXhu8I2w2xZanaxno4nXVDiYtEc+Mh88xnB7qPEkjkcgK5DtntlZ9t7OuLFecn3Ocv0i63SQeKRNkHmVrJycZJwnOAD5kkmmUnN8sfy/C7m/SpQtoqtWWW/lj5fbot/YxtntlaNt7S5GivOT7nOX6RdLpIPFImyDzK1k5OMk4TnAB8ySTzUeOKYPlWfHkKsjFRWFoadWrKrJzm8tmaUpWRgKUpQGk+dQl1ev1b1B763/wCdXV2nzqEur1+reoPfW/8Azq6uofV7EF2o+in8q1VpR9FP5VqqkkUpSgFKUoBSlKAVtSGEyGy2rwNbtKA4HZrLryya81DdrxrGHcNLT40Nuz2du2dk9bnUdp26lP8AGe1DmUHmkYxgYA5x/wBDHcW/RdmrltztpEE3Vl71pqOUiQtOY1tiKmqT6U6rwIyDwp55I8+QVeUuJGnRnYcxhDzLyFNuNrTlK0kYII8wQcVFt06uHaqyxo1q0detd2+FEQUNtRdSPx0AFRUSUtcIJJUeZGfLwAqHCVRcqeO5fb1KdKTnNZxots9+xUu2e2Vp22tLkWM85Puc5fpF0ukg8UibIPMrWTk4yThOcAHzJJPNR/SoR9Xrpz8YbjfF03++nq9dOfjDcb4um/31aqCisRawVVKsqsnOby2Xdn+P9KZ/3f0qEfV66c/GG43xdN/vp6vXTn4w3G+Lpv8AfU/C+5GGS7s/7v6Uz/u/pUI+r105+MNxvi6b/fT1eunPxhuN8XTf76fC+5DJd2f939KZ/jUI+r105+MNxvi6b/fT1eunPxhuN8XTf76fC+5DJd2PbUP9XZHmxejTDStpSUydTXyWwR4rT6YtvP8AJTShX4fV66c/GG43xdN/vrh0/oN6usmrNPaLt961vJ28j2+W6/JXrmYwuFJ7RCkIajNJS33ytxRPiolalKSUgL4/+cfxS5/lnCv/ABdvcKkpSi5Sxl4TzhLK1ePXPpgvtq8aFTnccnoDpxMpCCHbepHHzU8pXNR/iDzr7x5eFQcx1fmmn2w4jWG4uD/3vm/31r9Xrpz8YbjfF03++vT/AI5/H/8AL/D4WCrOoor5mkn/AMUv93l9WYVa3xpueMZLuz/Gmf8Ad/SoR9Xrpz8YbjfF03++nq9dOfjDcb4um/317vwfuRXku7P+7+lM/wC7+lQj6vXTn4w3G+Lpv99PV66c/GG43xdN/vp8L7kMl3Z/3f0pn/dUI+r105+MNxvi6b/fT1eunPxhuN8XTf76fC+5DJdwyK88+gXuDqOB0dm9s9uYPpWrrxqe9yA+6g+jWyKZRSZTpxg8wQlPPJHgeSVbkLoU7XXfUd10Va92NaSL/ZmWXrjb2NbylyYaHuLslON8ZKOLhJGR7PaM/qsvV12O12uLaJGutwpRit9kHk6hcilQyTzSwEJPMnBVlWOWSAKxnQlJYUkjYtqtOk3OostaLbPfsiyds9srTttaXIsZ5yfc5y/SLpdJB4pE2QeZWsnJxknCc4APmSSeaj+lQj6vXTn4w3G+Lpv99PV66c/GG43xdN/vqVQUViLWCqpVlVk5zeWy7s/x/pTP+7+lQj6vXTn4w3G+Lpv99PV66c/GG43xdN/vqfhfcjDJd2f939KZ/wB39KhH1eunPxhuN8XTf76er105+MNxvi6b/fT4X3IZLuz/ALv6Uz/GoR9Xrpz8YbjfF03++nq9dOfjDcb4um/30+F9yGS78+eeVQj1en1b1B763/51dY9Xrpz8YbjfF03++u6uj30e4Gx8BVjsa7g5DcmPTlqnSVSHlPOnicUXFd5WVZUSok5J51nGCgm21oRnJQiPop/KtVaUDCQP4VqrXMhSlKAUpSgFKUoBSlKAVpKUnxSDWqlAaeBH7opwI/dFaqUBp4EfuinAj90VqpQGngR+6KcCP3RWqlAaeBH7opwI/dFaqUBp4Efuitp+Iw+nhWgf8q36UB1nbrVb9l4WstXau3Kuk2yTLg9f35F/ktCPZY/ZICmWlJQngYT2ZISc4zgc8k87s91tOoLZEvVkuES4QJzKJEWVFdS6080oZStC0khSSMEEHBrVeLRbNQWqZY7zb486BcGHIsqNIbDjTzS0lK0LSeSkkEgg+INdfa01nqHbbUOh9M6Z2qu9+tN+uJtcqVazHajWOMiO4tLi0rWnCR2aQAAE8IUAePgQudQdncCP3RTgR+6K0MSG5CeJByK3agGngR+6KcCP3RWqlAaeBH7orr/cfcTUmidS6Kstk2vvepoep7quBcbjAcYS1aGgw44HnQ4tJIygeWMBQBKyhC/u62jaivujdQWfQOqIlm1E7DfiQbi4wJSYEtTeW1ra4hxFPElXCT5g4I5Hc08zeEWODa9SXRu6XOPGaamzmovoyJLwSAt1LQUoNhRBPCCQM4qUDLOn7Gm7TdRWu0wo9yuaGW50xphKXpKWgoNBxYGVhIWoDJOASBX222EJSOJIJ/KtMWKiKjhTW/RsGngR+6KcCP3RWqlQDTwI/dFOBH7orVSgNPAj90U4EfuitVKA08CP3RTgR+6K1UoDTwI/dFAhI8EitVKAUpSgFKUoBSlKAUpSgFKUoBSlKAUpSgFKUoBSlKAUpSgFKUoBW1IYTIbLavA1u0oDgllsuvbJr7UN2u+sYdw0tcI0Nuz2du2dk9bnkdp26lP8Z7UOcSDzSMYwMAc+ZQ5kedGamRH23mXkBbbjawpK0nwII5EfxpMiRp8d2HLYQ8y8hTbja05StJGCCPMEHFdXuWWD0btnl2vZ3ayderfpiOBbtNWh5IkSAp0dpwLeV3lDjWs5JJwQMnAoDtmuAXrePTFh3bsWzcu235V4v9rl3WPKatT64LbbC20qSuQE8CSe09uE4SFFJW2Fbu4lx3Pc0rGkbSRbB/j5nwVPsX5bqWBDLyPShxNZIcDZVg4PgeWcVydaGrl3gkBaAUhWOYBIyM/yH/IVOAcd0ltto7QU+/z9E6fj2xzVV1cvV2U1kmTMWhKVOHJOMhA5DAHPAGTXMW2ko58I4vOtMVj0doN5zit6obApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUArSpIUkpPnWqlAfmahNtlR8eKt1thtrPAMZrcpQClKUApSlAKUpQClKUApSlAKUpQClKUApSlAKUpQClKUB//9k=)

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]

Output: [1,2,3,4]

Â 

Constraints:

- m == mat.length

- n == mat[i].length

- 1 <= m, n <= 104

- 1 <= m * n <= 104

- -105 <= mat[i][j] <= 105

**





## Solution

### Approach 1: Diagonal Iteration and Reversal

**Intuition**

A common strategy for solving a lot of programming problem is to first solve a stripped down, simpler version of them and then think what needs to be changed to achieve the original goal. Our first approach to this problem is also based on this very idea. So, instead of thinking about the zig-zag pattern of printing for the diagonals, let's say the problem statement simply asked us to print out the contents of the matrix, one diagonal after the other starting from the first element. Let's see what this problem would look like.

![](https://leetcode.com/problems/diagonal-traverse/solutions/459889/Figures/498/img1.png)

The first row and the last column in this problem would serve as the starting point for the corresponding diagonal. Given an element inside a diagonal, say [i,j], we can either go up the diagonal by going one row up and one column ahead i.e. [i−1,j+1] or, we can go down the diagonal by going one row down and one column to the left i.e. [i+1,j−1]. *Note* that this applies to diagonals that go from `right to left` only. The math would change for the ones that go from left to right.

This is a simple problem to solve, right? The only difference between this one and the original problem is that some of the diagonals are not printed in the right order. That's all we need to fix to get the right solution!

> We simply need to reverse the odd numbered diagonals before we add the elements to the final result array. So, for e.g. the third diagonal starting from the left would be [3, 7, 11] and before we add these elements to the final result array, we simply reverse them i.e. [11, 7, 3].

**Algorithm**

1. Initialize a `result` array that we will eventually return.

2. We would have an outer loop that will go over each of the diagonals one by one. As mentioned before, the elements in the first row and the last column would actually be the heads of their corresponding diagonals.

3. We then have an inner while loop that iterates over all the elements in the diagonal. We can calculate the number of elements in the corresponding diagonal by doing some math but we can simply iterate until one of the indices goes out of bounds.

4. For each diagonal we will need a new list or dynamic array like data structure since we don't know what size to allocate. Again, we can do some math and calculate the size of that particular diagonal and allocate memory; but it's not necessary for this explanation.

5. For odd numbered diagonals, we simply need to add the elements in our intermediary array, in reverse order to the final result array.
   
   ![](https://leetcode.com/problems/diagonal-traverse/solutions/459889/Figures/498/img2.png)





class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {

        // Check for empty matrices
        if (matrix == null || matrix.length == 0) {
            return new int[0];
        }
    
        // Variables to track the size of the matrix
        int N = matrix.length;
        int M = matrix[0].length;
    
        // The two arrays as explained in the algorithm
        int[] result = new int[N*M];
        int k = 0;
        ArrayList<Integer> intermediate = new ArrayList<Integer>();
    
        // We have to go over all the elements in the first
        // row and the last column to cover all possible diagonals
        for (int d = 0; d < N + M - 1; d++) {
    
            // Clear the intermediate array every time we start
            // to process another diagonal
            intermediate.clear();
    
            // We need to figure out the "head" of this diagonal
            // The elements in the first row and the last column
            // are the respective heads.
            int r = d < M ? 0 : d - M + 1;
            int c = d < M ? d : M - 1;
    
            // Iterate until one of the indices goes out of scope
            // Take note of the index math to go down the diagonal
            while (r < N && c > -1) {
    
                intermediate.add(matrix[r][c]);
                ++r;
                --c;
            }
    
            // Reverse even numbered diagonals. The
            // article says we have to reverse odd 
            // numbered articles but here, the numbering
            // is starting from 0 :P
            if (d % 2 == 0) {
                Collections.reverse(intermediate);
            }
    
            for (int i = 0; i < intermediate.size(); i++) {
                result[k++] = intermediate.get(i);
            }
        }
        return result;
    }

}



**Complexity Analysis**

- Time Complexity: O(N⋅M) considering the array has N rows and M columns. An important thing to remember is that for all the odd numbered diagonals, we will be processing the elements twice since we have to reverse the elements before adding to the result array. Additionally, to save space, we have to `clear` the intermediate array before we process a new diagonal. That operation also takes O(K) where K is the size of that array. So, we will be processing all the elements of the array at least twice. But, as far as the asymptotic complexity is concerned, it remains the same.
- Space Complexity: O(min(N,M)) since the extra space is occupied by the intermediate arrays we use for storing diagonal elements and the maximum it can occupy is the equal to the minimum of N and M. Remember, the diagonal can only extend till one of its indices goes out of scope.  

---

### Approach 2: Simulation

**Intuition**

This approach simply and plainly does what the problem statement asks us to do. It's pure simulation. However, in order to implement this simulation, we need to understand the walking patterns inside the array. Basically, in the previous approach, figuring out the `head` of the diagonal was pretty easy. In this case, it won't be that easy. We need to figure out two things for each diagonal:

1. The direction in which we want to process it's elements and
2. The head or the starting point for the diagonal `depending upon its direction`.

Let's see these two things annotated on a sample matrix.

![](https://leetcode.com/problems/diagonal-traverse/solutions/459889/Figures/498/img3.png)

Now that we know what two things we need to figure out, let's get to the part where we actually do it! The direction is pretty straightforward. We can simply use a boolean variable and keep alternating it to figure out the direction for a diagonal. That part is sorted. The slightly tricky part is figuring out the head of the next diagonal.

The good part is, we already know the `end` of the previous diagonal. We can use that information to figure out the head of the next diagonal.

**Next head when going UP**  

Let's look at the two scenarios that we may come across when we are at the tail end of a downwards diagonal and we want to find the head of the next diagonal.

![](https://leetcode.com/problems/diagonal-traverse/solutions/459889/Figures/498/img4.png)

So, the general rule that we will be following when we want to find the head for an upwards going diagonal is that:

> The head would be the node directly below the tail of the previous diagonal. Unless the tail lies in the last row of the matrix in which case the head would be the node right next to the tail.

**Next head when going DOWN**  

Let's look at the two scenarios that we may come across when we are at the tail end of an upwards diagonal and we want to find the head of the next diagonal.

![](https://leetcode.com/problems/diagonal-traverse/solutions/459889/Figures/498/img5.png)

So, the general rule that we will be following when we want to find the head for a downwards going diagonal is that:

> The head would be the node to the right of the tail of the previous diagonal. Unless the tail lies in the last column of the matrix in which case the head would be the node directly below the tail.

**Algorithm**

1. Initialize a boolean variable called `direction` which will tell us whether the current diagonal is an upwards or downwards going. Based on the current direction and the tail, we will determine the head of the next diagonal. Initially the direction would be `1` which would indicate `up`. We will keep alternating this value from one iteration to the next.

2. Assuming we know the head of a diagonal, say matrix[i][j], we will use the direction to progress along the diagonal and process its elements.
   
   - For an upwards going diagonal, the next element in the diagonal would be matrix[i−1][j+1]
   - For a downwards going diagonal, the next element would be matrix[i+1][j−1].

3. We keep processing the elements of the current diagonal until we go out of the boundaries of the matrix.

4. Now, given that we know the tail of the diagonal (the last node before we went out of bounds), let's see how we can find the next head. Note that in the following pseudocode, the `direction` is for the current diagonal and we are trying to find the head of the next diagonal. So, if the direction is `up`, it means the next diagonal would be going down and vice-versa.
   
   tail = [i, j]
   if direction == up, then {
     if [i, j + 1] is within bounds, then {
   
         next_head = [i, j + 1]
   
     } else { 
   
         next_head = [i + 1, j]
   
     }
   } else {
     if [i + 1, j] is within bounds, then {
   
         next_head = [i + 1, j]
   
     } else { 
   
         next_head = [i, j + 1]
   
     }
   }

5. We keep processing the elements of a diagonal and once the current diagonal ends, we use the current direction and the tail element to find the next head and we switch over to processing the next diagonal. Also remember to flip the direction bit.



class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {

        // Check for empty matrices
        if (matrix == null || matrix.length == 0) {
            return new int[0];
        }
    
        // Variables to track the size of the matrix
        int N = matrix.length;
        int M = matrix[0].length;
    
        // Incides that will help us progress through 
        // the matrix, one element at a time.
        int row = 0, column = 0;
    
        // As explained in the article, this is the variable
        // that helps us keep track of what direction we are
        // processing the current diaonal
        int direction = 1;
    
         // The final result array
        int[] result = new int[N*M];
        int r = 0;
    
        // The uber while loop which will help us iterate over all
        // the elements in the array.
        while (row < N && column < M) {
    
            // First and foremost, add the current element to 
            // the result matrix. 
            result[r++] = matrix[row][column];
    
            // Move along in the current diagonal depending upon
            // the current direction.[i, j] -> [i - 1, j + 1] if 
            // going up and [i, j] -> [i + 1][j - 1] if going down.
            int new_row = row + (direction == 1 ? -1 : 1);
            int new_column = column + (direction == 1 ? 1 : -1);
    
            // Checking if the next element in the diagonal is within the
            // bounds of the matrix or not. If it's not within the bounds,
            // we have to find the next head. 
            if (new_row < 0 || new_row == N || new_column < 0 || new_column == M) {
    
                // If the current diagonal was going in the upwards
                // direction.
                if (direction == 1) {
    
                    // For an upwards going diagonal having [i, j] as its tail
                    // If [i, j + 1] is within bounds, then it becomes
                    // the next head. Otherwise, the element directly below
                    // i.e. the element [i + 1, j] becomes the next head
                    row += (column == M - 1 ? 1 : 0) ;
                    column += (column < M - 1 ? 1 : 0);
    
                } else {
    
                    // For a downwards going diagonal having [i, j] as its tail
                    // if [i + 1, j] is within bounds, then it becomes
                    // the next head. Otherwise, the element directly below
                    // i.e. the element [i, j + 1] becomes the next head
                    column += (row == N - 1 ? 1 : 0);
                    row += (row < N - 1 ? 1 : 0);
                }
    
                // Flip the direction
                direction = 1 - direction;        
    
            } else {
    
                row = new_row;
                column = new_column;
            }
        }
        return result;      
    }

}





**Complexity Analysis**

- Time Complexity: O(N⋅M) since we process each element of the matrix exactly once.
- Space Complexity: O(1) since we don't make use of any additional data structure. Note that the space occupied by the output array doesn't count towards the space complexity since that is a requirement of the problem itself. Space complexity comprises any `additional` space that we may have used to get to build the final array. For the previous solution, it was the intermediate arrays. In this solution, we don't have any additional space apart from a couple of variables.
