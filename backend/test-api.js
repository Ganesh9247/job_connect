async function test() {
    try {
        console.log("Registering...");
        const regRes = await fetch('https://job-connect-backend-l8qg.onrender.com/api/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                fullName: "Test User",
                email: "test81@test.com",
                password: "password123",
                phone: "1234567890",
                role: "ROLE_JOB_SEEKER"
            })
        });
        const regData = await regRes.text();
        console.log("Register Response:", regRes.status, regData);
    } catch (e) {
        console.log("Register Failed:", e);
    }

    try {
        console.log("\nLogging in...");
        const loginRes = await fetch('https://job-connect-backend-l8qg.onrender.com/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                email: "test81@test.com",
                password: "password123"
            })
        });
        const loginData = await loginRes.text();
        console.log("Login Response:", loginRes.status, loginData);
    } catch (e) {
        console.log("Login Failed:", e);
    }
}

test();
