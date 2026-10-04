MIME

puppeteer version 5.2.1 using chrome 85.0.4182.0
https://source.chromium.org/chromium/chromium/src/+/refs/tags/85.0.4182.0:



puppeteer sẽ đến `url + '#/login'`
```javascript
<script>
export default {
  data() {
    return { form: { uid: "", upw: "" } };
  },
  created() {
    // login() is deliberately exposed on the global window object.
    window.login = this.login;
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      this.login(this.form);
    },
    login(form) {
      this.$http
        .post("/login", form)
        .then((res) => {
          this.$cookie.set("token", res.data.token);
          location.href = "/";
        })
        .catch((err) => {
          alert(err.response.data);
        });
    },
  },
};
</script>
```
Code phía trên sẽ load vào dom `window.login = this.login;`
login bây giờ sẽ đóng vai trò là global sau đó puppeteer gọi `javascript:login({"uid": "admin", "upw": "${jwt.secret}"})` hàm login sẽ được thực thi
```javascript
router.post('/login', function(req, res, next) {
    const {
        uid,
        upw
    } = req.body;

    var user = login(uid, upw);
    if (user) {
        if (uid == 'admin') {
            if (jwt.isadmin(req.connection.remoteAddress)) {
                res.send({
                    'token': jwt.sign(user, jwt.secret, {
                        expiresIn: jwt.exp['admin']
                    })
                });
            } else {
                res.status(403).send('noperm');
            }
        } else {
            res.send({
                'token': jwt.sign(user, jwt.secret, {
                    expiresIn: jwt.exp['user']
                })
            });
        }
    } else {
        res.status(403).send('check id/pw');
    }
});
```

Lúc này thì do puppeteer đang chạy ở local nên token admin sẽ được trả về trong response và bây giờ token sẽ được gán trong `header token` bởi `this.$cookie.set("token", res.data.token);` và điều hướng tới `/`

Tiếp đến puppeteer sẽ go to `input_url = url + path;`

Lúc này cũng không thể gửi được cookie của admin về attacker server vì token không được trình duyệt gửi đi mà cần có hàm javascript ấy token và gửi lên server
