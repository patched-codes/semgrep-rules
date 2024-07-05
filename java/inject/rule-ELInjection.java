// License: MIT (c) GitLab Inc.

import javax.el.ELContext;
import javax.el.ELProcessor;
import javax.el.ExpressionFactory;
import javax.el.MethodExpression;
import javax.faces.context.FacesContext;
import javax.enterprise.context.RequestScoped;
import javax.inject.Named;

// Rule: java_inject_rule-ELInjection
@Named
@RequestScoped
class ElInjectionBean {

    private String userInputValue, userInputMethod, userInputLambda,
            userInputELProcessor, userInputLambdaArgs, userInputELProcessorGV, userInputELProcessorSV,
            inputValueToSet;

    private Object evaluationVResult, evaluationMResult, evaluationLResult,
            evaluationELPResult, evaluationELPGetValue, evaluationELPSetValue;

    private String lambdaExpression, privateConfigValue;

    public void evaluateValueExpression() {

        try {
            FacesContext facesContext = FacesContext.getCurrentInstance();
            ELContext elContext = facesContext.getELContext();
            ExpressionFactory expressionFactory = facesContext.getApplication().getExpressionFactory();

            System.out.println("User input: " + userInputValue);
            // ruleid: java_inject_rule-ELInjection
            evaluationVResult = expressionFactory.createValueExpression(elContext, userInputValue, Object.class)
                    .getValue(elContext);

            // ok: java_inject_rule-ELInjection
            evaluationVResult = expressionFactory.createValueExpression(elContext, "#{2+2}", Object.class)
                    .getValue(elContext);
            System.out.println("Evaluation Result: " + evaluationVResult);

        } catch (Exception e) {
            evaluationVResult = "Error: " + e.getMessage();
        }
    }

    public void evaluateMethodExpression() {

        try {
            FacesContext facesContext = FacesContext.getCurrentInstance();
            ELContext elContext = facesContext.getELContext();
            ExpressionFactory expressionFactory = facesContext.getApplication().getExpressionFactory();

            System.out.println("User input: " + userInputMethod);

            // ruleid: java_inject_rule-ELInjection
            MethodExpression methodExpression = expressionFactory.createMethodExpression(
                    elContext, userInputMethod, Object.class, new Class<?>[0]);

            // Evaluate the MethodExpression
            evaluationMResult = methodExpression.invoke(elContext, null);

            // ok: java_inject_rule-ELInjection
            MethodExpression methodExpression2 = expressionFactory.createMethodExpression(
                    elContext, "#{elInjectionBean.getSum}", Object.class, new Class<?>[0]);

            // Evaluate the MethodExpression
            evaluationMResult = methodExpression2.invoke(elContext, null);

            System.out.println("Evaluation Result: " + evaluationMResult);

        } catch (Exception e) {
            evaluationMResult = "Error: " + e.getMessage();
        }
    }

    public int getSum() {
        return 10 + 20;
    }

    public void evaluateELProcessor() {
        ELProcessor elProcessor = new ELProcessor();
        try {
            // ruleid: java_inject_rule-ELInjection
            evaluationELPResult = elProcessor.eval(userInputELProcessor);

            // ok: java_inject_rule-ELInjection
            evaluationELPResult = elProcessor.eval("2*2");
        } catch (Exception e) {
            evaluationELPResult = "Error: " + e.getMessage();
        }
    }

    public void evaluateELProcessorGetValue() {
        ELProcessor elProcessor = new ELProcessor();
        try {
            // ruleid: java_inject_rule-ELInjection
            evaluationELPGetValue = elProcessor.getValue(userInputELProcessorGV, Object.class);

            // ok: java_inject_rule-ELInjection
            evaluationELPGetValue = elProcessor.getValue("2+2", Object.class);
        } catch (Exception e) {
            evaluationELPGetValue = "Error in getValue: " + e.getMessage();
        }
    }

    public void evaluateELProcessorSetValue() {
        ELProcessor elProcessor = new ELProcessor();
        try {
            // Define 'elInjectionBean' within ELProcessor's context
            elProcessor.defineBean("elInjectionBean", this);

            // ruleid: java_inject_rule-ELInjection
            elProcessor.setValue(userInputELProcessorSV, inputValueToSet);
            evaluationELPSetValue = "Expression : " + userInputELProcessorSV + " Value : " + inputValueToSet;

            // ok: java_inject_rule-ELInjection
            elProcessor.setValue("userInputELProcessorSV.privateConfigValue", "inputValueToSet");
        } catch (Exception e) {
            evaluationELPSetValue = "Error in setValue: " + e.getMessage();
        }
    }

}
