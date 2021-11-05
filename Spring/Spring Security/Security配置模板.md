```java
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // 退出登录设置
        http.logout()
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login").permitAll();

        // 登录设置
        http.formLogin()
                .loginPage("/login.html")
                .passwordParameter("pwd")
                .usernameParameter("user")
                .successHandler(new MyAuthenticationSuccessHandler("http://baidu.com"))
                .loginProcessingUrl("/login")
                .failureHandler(new MyAuthenticationFailureHandler("http://baidu.com"));

        // 授权设置
        http.authorizeRequests()
                .antMatchers(HttpMethod.GET,"/login.html","/login").permitAll()
                .antMatchers("/test").hasAnyAuthority("admin","user")
                .anyRequest().authenticated();

        // remember设置
        http.rememberMe()
                .tokenRepository(persistentTokenRepository())
                .userDetailsService(myUserDetailsService)
                .tokenValiditySeconds(60);

        // csrf设置
        http.csrf()
//                .csrfTokenRepository(csrfTokenRepository());
        .disable();
    }
```

