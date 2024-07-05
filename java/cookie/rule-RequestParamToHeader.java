// License: MIT (c) GitLab Inc.
package cookie;

import org.apache.commons.text.StringEscapeUtils;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletResponseWrapper;
import java.io.IOException;

public class RequestParamToHeader extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String input = req.getParameter("input");
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", input);
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.setHeader("CUSTOM_HEADER", input);

        String paramNames = req.getParameterNames().nextElement();
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", paramNames);
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.setHeader("CUSTOM_HEADER", paramNames);

        String paramValues = req.getParameterValues("input")[0];
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", paramValues);

        String paramMap = req.getParameterMap().get("input")[0];
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", paramMap);

        String header = req.getHeader("input");
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", header);
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.setHeader("CUSTOM_HEADER", header);

        String contextPath = req.getPathInfo();
        Cookie cPath = new Cookie("name", null);
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", contextPath);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String input = req.getParameter("input");
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", input);

        String header = req.getHeader("input");
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", header);
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.setHeader("CUSTOM_HEADER", header);

        String contextPath = req.getPathInfo();
        Cookie cPath = new Cookie("name", null);
        //ruleid: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", contextPath);

        String tainted = req.getParameter("input");
        HttpServletResponseWrapper wrapper = new HttpServletResponseWrapper(resp);
        //ruleid: java_cookie_rule-RequestParamToHeader
        wrapper.addHeader("test", tainted);
        //ruleid: java_cookie_rule-RequestParamToHeader
        wrapper.setHeader("test2", tainted);
    }

    @Override
    protected void doPut(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String data = req.getParameter("input");
        String input = data.replaceAll("[\r\n]+", "");
        //ok: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", input);
        //ok: java_cookie_rule-RequestParamToHeader
        resp.setHeader("CUSTOM_HEADER", input);

        String header = req.getHeader("input");
        header = header.replaceAll("[\r\n]+", "");
        //ok: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", header);
        //ok: java_cookie_rule-RequestParamToHeader
        resp.setHeader("CUSTOM_HEADER", header);

        String contextPath = req.getPathInfo();
        contextPath = contextPath.replaceAll("[\r\n]+", "");
        //ok: java_cookie_rule-RequestParamToHeader
        resp.addHeader("CUSTOM_HEADER", contextPath);

    }

}
