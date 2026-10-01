def money(value):
    return f"₹{value:,.2f}"


def build_budget_plan(data):
    income = data["income"]
    expenses = {
        "Housing": data["housing"],
        "Food": data["food"],
        "Transport": data["transport"],
        "Utilities": data["utilities"],
        "Entertainment": data["entertainment"],
        "Other": data["other"],
    }

    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    savings_goal = data["savings_goal"]

    if income <= 0:
        raise ValueError("Income must be greater than zero.")

    expense_percent = (total_expenses / income) * 100
    savings_percent = (max(remaining, 0) / income) * 100

    recommendations = []

    if remaining < 0:
        recommendations.append(
            "Your expenses are higher than your income. Reduce flexible spending "
            "and review recurring expenses first."
        )
    else:
        if savings_goal > remaining:
            recommendations.append(
                f"Your current monthly surplus is {money(remaining)}, which is below "
                f"your savings goal of {money(savings_goal)}. Consider lowering "
                "non-essential expenses or adjusting the goal."
            )
        else:
            recommendations.append(
                f"You can currently set aside about {money(remaining)} per month. "
                "Keep an emergency fund as a priority before increasing optional spending."
            )

    if income > 0 and data["housing"] / income > 0.35:
        recommendations.append(
            "Housing is taking a relatively large share of income. If practical, "
            "look for ways to reduce housing-related costs."
        )

    if income > 0 and data["food"] / income > 0.15:
        recommendations.append(
            "Food spending is relatively high compared with income. Planning meals "
            "and comparing grocery prices may help."
        )

    if income > 0 and data["entertainment"] / income > 0.10:
        recommendations.append(
            "Entertainment is a flexible category. Setting a monthly limit can create "
            "more room for savings."
        )

    if remaining >= 0 and savings_percent >= 20:
        status = "Strong monthly surplus"
    elif remaining >= 0:
        status = "Positive monthly surplus"
    else:
        status = "Monthly deficit"

    largest_category = max(expenses, key=expenses.get)

    return {
        "total_expenses": total_expenses,
        "remaining": remaining,
        "expense_percent": expense_percent,
        "savings_percent": savings_percent,
        "status": status,
        "largest_category": largest_category,
        "recommendations": recommendations,
        "money": money,
    }
