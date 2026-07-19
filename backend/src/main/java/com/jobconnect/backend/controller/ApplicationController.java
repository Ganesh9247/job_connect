package com.jobconnect.backend.controller;

import com.jobconnect.backend.entity.Application;
import com.jobconnect.backend.entity.Job;
import com.jobconnect.backend.entity.User;
import com.jobconnect.backend.repository.ApplicationRepository;
import com.jobconnect.backend.repository.JobRepository;
import com.jobconnect.backend.repository.UserRepository;
import com.jobconnect.backend.security.CustomUserDetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/applications")
public class ApplicationController {

    @Autowired
    private ApplicationRepository applicationRepository;

    @Autowired
    private JobRepository jobRepository;

    @Autowired
    private UserRepository userRepository;

    @PostMapping("/apply/{jobId}")
    public ResponseEntity<?> applyForJob(@PathVariable Long jobId) {
        CustomUserDetails userDetails = (CustomUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        Long userId = userDetails.getId();

        if (applicationRepository.existsByJobIdAndUserId(jobId, userId)) {
            return ResponseEntity.badRequest().body("You have already applied for this job.");
        }

        Job job = jobRepository.findById(jobId).orElseThrow(() -> new RuntimeException("Job not found"));
        User user = userRepository.findById(userId).orElseThrow(() -> new RuntimeException("User not found"));

        Application application = new Application();
        application.setJob(job);
        application.setUser(user);
        application.setStatus("APPLIED");

        applicationRepository.save(application);

        return ResponseEntity.ok("Applied successfully.");
    }

    @GetMapping("/my")
    public ResponseEntity<List<Application>> getMyApplications() {
        CustomUserDetails userDetails = (CustomUserDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        return ResponseEntity.ok(applicationRepository.findByUserId(userDetails.getId()));
    }
}
