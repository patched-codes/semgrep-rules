package com.test.servlet.openredirect;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class UnvalidatedRedirect extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String c = request.getParameter("case");

        String url = "";

        if (c.equals("1")) {
            url = request.getParameter("redirectTo");
            if (url != null) {
                // ruleid: java_endpoint_rule-UnvalidatedRedirect
                response.sendRedirect(url);
            }

        } else if (c.equals("2")) {

            url = request.getParameter("redirectTo");
            if (url != null) {
                // ruleid: java_endpoint_rule-UnvalidatedRedirect
                response.addHeader("Location", url);
                response.sendError(302);
            }

        } else if (c.equals("3")) {

            url = "/ServletSample/UnvalidatedRedirect";
            if (url != null) {
                // ok: java_endpoint_rule-UnvalidatedRedirect
                response.sendRedirect(url);
            }

        } else if (c.equals("4")) {

            // ok: java_endpoint_rule-UnvalidatedRedirect
            response.addHeader("Location", "/ServletSample/UnvalidatedRedirect");
            response.sendError(302);

        } else if (c.equals("6")) {

            List<String> safeUrls = new ArrayList<>();
            safeUrls.add("/ServletSample/UnvalidatedRedirect");
            safeUrls.add("/ServletSample/");

            String redirectUrl = request.getParameter("redirectTo");

            if (safeUrls.contains(redirectUrl)) {
                // ok: java_endpoint_rule-UnvalidatedRedirect
                response.sendRedirect(redirectUrl);
            } else {
                response.sendError(404);
            }
        }

    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String c = request.getParameter("case");

        String url = "";

        if (c.equals("5")) {

            url = request.getParameter("url");
            if (url != null && !url.isEmpty()) {
                // ruleid: java_endpoint_rule-UnvalidatedRedirect
                response.sendRedirect(url);
            }
        }
    }

}
