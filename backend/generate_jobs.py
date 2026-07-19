import os

base_dir = "src/main/java/com/jobconnect/backend"
controller_dir = f"{base_dir}/controller"

job_controller = """package com.jobconnect.backend.controller;

import com.jobconnect.backend.entity.Job;
import com.jobconnect.backend.repository.JobRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/jobs")
public class JobController {
    
    @Autowired
    private JobRepository jobRepository;

    @GetMapping("/public")
    public ResponseEntity<List<Job>> getAllJobs() {
        return ResponseEntity.ok(jobRepository.findAll());
    }
    
    @GetMapping("/public/{id}")
    public ResponseEntity<Job> getJobById(@PathVariable Long id) {
        return jobRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
"""

with open(f"{controller_dir}/JobController.java", "w") as f:
    f.write(job_controller)

print("JobController generated successfully.")
