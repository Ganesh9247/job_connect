async function test() {
    try {
        console.log("Registering...");
        const regRes = await fetch('https://job-connect-backend-l8qg.onrender.com/api/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                fullName: "John",
                email: "john@123gmail.com",
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
}

test();
